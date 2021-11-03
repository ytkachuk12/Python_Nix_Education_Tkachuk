-- Добавить 2 триггера
-- (один из них ДО операции по изменению данных, второй после)
-- и функции или процедуры-обработчики к ним.

-- create new table for old car numbers
CREATE TABLE old_numbers (
   id SERIAL PRIMARY KEY ,
   car_id INT NOT NULL,
   old_namber VARCHAR(40) NOT NULL,
   changed_date TIMESTAMP(6) NOT NULL,
   FOREIGN KEY (car_id) REFERENCES car(car_id)
);

-- create index
CREATE INDEX idx_old_numbers_old_namber ON old_numbers(old_namber);


-- func for trigger
CREATE OR REPLACE FUNCTION Check_car_number()
    RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
    BEGIN
        if NEW.car_namber = OLD.car_namber then
            RAISE notice 'Its the same number';
            rollback ;
        else
            INSERT INTO old_numbers(id, car_id, old_namber, changed_date)
		    VALUES(1, OLD.car_id, OLD.car_namber, now());

        end if;

        RETURN NEW;
    end;
$$;
end;

-- trigger before update on table car
CREATE TRIGGER update_car_number
  BEFORE UPDATE
  ON car
  FOR EACH ROW
  EXECUTE PROCEDURE Check_car_number();


-- func for trigger
CREATE OR REPLACE FUNCTION re_update_index()
    RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
    begin
        REINDEX INDEX idx_old_numbers_old_namber;
        return new;
    end;
$$;
end ;

-- trigger after update on table car
CREATE TRIGGER reindex_after_update
    AFTER UPDATE
    ON car
    FOR STATEMENT
    EXECUTE PROCEDURE re_update_index();

-- update car number
UPDATE car
SET car_namber = '3465878'
WHERE car_id = 2;