

DB_NAME = 'Purbeurre'
TABLES = {}

create database if not exists Purbeurre character set 'utf8';

use Purbeurre;

TABLES['Food'] = ( 
	"create table Food("
	"id int unsigned auto_increment not null primary key,"
	"name varchar(130)) not null unique,"
	"category_id int unsigned not null,"
	"nutriscore varchar(1) not null,"
	"description varchar(1000) not null,"
	"store varchar(100) not null,"
	"link varchar(300) not null"
	") engine = InnoDB;"


TABLES['Category'] = (
	"create table category("
	"id int unsigned auto_increment not null primary key,"
	"categories varchar(50) not null unique"
	");"

TABLES['Favorite'] = (
	"create table Favorite("
	"id int unsigned auto_increment not null primary key,"
	"id_food int unsigned not null,"
	"id_substitute int unsigned not null,"
	"unique uni_food_substitute (id_food, id_substitute)"
	")engine = InnoDB;"

alter table Food
add index ind_nutriscore (nutriscore);

alter table Food
add constraint fk_food_category foreign key (category_id) references category (id);

alter table Favorite 
add constraint fk_favorite_food foreign key (id_food) references Food (id);

alter table Favorite
add constraint fk_favorite_substitute foreign key (id_substitute) references Food (id);

