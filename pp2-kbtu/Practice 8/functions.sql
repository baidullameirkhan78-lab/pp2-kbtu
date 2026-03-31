-- Функция 1: паттерн бойынша іздеу
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM phonebook c
        WHERE c.name  ILIKE '%' || p_pattern || '%'
           OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- Функция 2: пагинация
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM phonebook c
        ORDER BY c.id
        LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;