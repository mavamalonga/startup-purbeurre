
TABLES = {}

TABLES['Product'] = ( 
	"create table Product("
	"id int unsigned auto_increment not null primary key,"
	"product_name varchar(100) not null unique,"
	"brands varchar(100) null,"
	"category_id int unsigned not null,"
	"ingredients_text varchar(500) not null,"
	"nutrition_grades varchar(1) not null,"
	"nutriments varchar(500) not null,"
	"quantity varchar(10) not null,"
	"store varchar(100) not null,"
	"link varchar(300) not null"
	") engine = InnoDB;"
)

TABLES['Category'] = (
	"create table category("
	"id int unsigned auto_increment not null primary key,"
	"categories varchar(50) not null unique"
	");"
	)

TABLES['Favorite'] = (
	"create table Favorite("
	"id int unsigned auto_increment not null primary key,"
	"product_id int unsigned not null,"
	"substitute_id int unsigned not null,"
	"unique uniq_product_substitute (product_id, substitute_id)"
	")engine = InnoDB;"
	)

TABLES['Ind_nutri-score'] = (
	"alter table Product add index ind_nutri_score(nutrition_grades);"
	)

TABLES['Fk_favorite_category'] = (
	"alter table Product add constraint fk_product_category foreign key (category_id) references category (id);"
	)

TABLES['Fk_favorite_product'] = (
	"alter table Favorite add constraint fk_favorite_product foreign key (product_id) references Product (id);"
	)

TABLES['Fk_favorite_substitute'] = (
	"alter table Favorite add constraint fk_favorite_substitute foreign key (substitute_id) references Product (id);"
	)

