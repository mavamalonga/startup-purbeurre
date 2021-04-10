
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


--procedure check the number of the requested product then select the product
	create procedure select_product_id(in p_category_id int, in p_product_id int)
		begin
			declare v_nb int;
			select count(id) into v_nb
			from product
			where id = p_product_id and category_id = p_category_id;

			if v_nb = 0 then
				select 'empty';
			else
				select product_name, brands, substring(ingredients_text, 1, 60), 
				substring(nutriments, 1, 60), nutrition_grades,
				quantity, store
				from product
				where id = p_category_id and category_id = p_category_id;
			end if;
		end |


--procedure select 5 product from the same category as p_product_id with better nutrition grade than p_product_id
	create procedure select_substitute_list(in p_category_id int, in p_product_id int)
		begin
			declare v_nb int;
			select count(id) into v_nb
			from product
			where id != p_product_id and category_id = p_category_id and nutrition_grades <= (
				select nutrition_grades
				from product 
				where id = p_product_id 
				);

			if v_nb = 0 then
				select 'empty';
			else
				select id, product_name, nutrition_grades
				from product
				where id != p_product_id and category_id = p_category_id and nutrition_grades <= (
					select nutrition_grades
					from product
					where id = p_product_id
					)
				order by nutrition_grades
				limit 5;
			end if;
		end |



--	procedure checks the entered substitute number then selects the substitute character
	create procedure select_substitute(in p_category_id int,in p_product_id int, in p_substitute_id int)
		begin

			declare v_nutrition char(1);
			declare v_nb int;

			select nutrition_grades into v_nutrition
			from product
			where id = p_product_id;


			select count(id) into v_nb
			from product
			where id = p_substitute_id and category_id = p_category_id and p_substitute_id in 
				(	select id
					from product
					where id != p_product_id and category_id = p_category_id and nutrition_grades <= v_nutrition
					);

			if v_nb = 0 then
				select 'empty';
			else
				select product_name, brands, substring(ingredients_text, 1, 60), 
				substring(nutriments, 1, 60), nutrition_grades,
				quantity, store
				from product
				where id = p_substitute_id;
			end if;

		end |