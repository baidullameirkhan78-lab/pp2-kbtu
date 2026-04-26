-- 1. Жаңа телефон қосу процедурасы
CREATE OR REPLACE PROCEDURE add_phone(
    p_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE first_name = p_name;
    
    IF v_contact_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
    ELSE
        RAISE EXCEPTION 'Контакт % табылмады!', p_name;
    END IF;
END;
$$;

-- 2. Кеңейтілген іздеу функциясы (Python-дағы 11-ші пункт үшін)
CREATE OR REPLACE FUNCTION search_contacts(p_query VARCHAR)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.first_name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;

-- 3. Пагинация (беттеу) функциясы
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.email, c.birthday, g.name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;