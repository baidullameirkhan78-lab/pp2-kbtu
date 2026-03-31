-- Процедура 1: upsert
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- Процедура 2: жою
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;


-- Процедура 3: топтық енгізу + телефон тексеру
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    v_name  TEXT;
    v_phone TEXT;
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        v_name  := p_names[i];
        v_phone := p_phones[i];

        IF v_phone ~ '^\+?[0-9\-\s]{7,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = v_name) THEN
                UPDATE phonebook SET phone = v_phone WHERE name = v_name;
            ELSE
                INSERT INTO phonebook(name, phone) VALUES (v_name, v_phone);
            END IF;
        ELSE
            RAISE NOTICE 'Қате телефон: % -> %', v_name, v_phone;
        END IF;
    END LOOP;
END;
$$;