
-- procedure which checks the availability of the category then selects all the males of the database
create procedure select_categories()
	begin
		declare v_nb int;

		select count(id) into v_nb
		from category;

		if v_nb = 0 then
			select 'empty';
		else
			select id, categories
			from category
			order by id;
		end if;
	end |


--procedure which checks the availability of products of category with index p_category_id then selects all the products
create procedure select_products_list(p_category_id int)
	begin
		declare v_nb int;

		select count(id) into v_nb
		from product 
		where category_id = p_category_id;

		if v_nb = 0 then
			select 'empty';
		else
			select id, product_name
			from product
			where category_id = p_category_id
			order by id
			limit 20;
		end if;
	end |



