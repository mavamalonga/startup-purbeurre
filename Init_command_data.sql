create database if not exists Purbeurre character set 'utf8';

use Purbeurre;


create table Food(
id int unsigned auto_increment not null primary key,
name_food varchar(130) not null unique,
category_id int unsigned not null,
nutriscore varchar(1) not null,
description varchar(1000) not null,
store varchar(100) not null,
link varchar(300) not null
)
engine = InnoDB;

create table Favorite(
id int unsigned auto_increment not null primary key,
id_food int unsigned not null,
id_substiutue_chooses int unsigned not null,
unique unique_id_food_substance_chooses (id_food, id substitue_chooses)
)
engine = InnoDB;

create table Category(
id int unsigned auto_increment not null primary key,
categories varchar(50) not null unique
)

alter table Food
add index ind_nutriscore (nutriscore);

alter table Food
add constraint fk_favorite_id_category foreign key (category_id) references Food (id);

alter table Favorite
add constraint fk_favorite_id_food foreign key (id_food) references Food (id);

alter table Favorite
add constraint fk_favorite_substitue_chooses foreign key (id_substitute_chooses) references Food (id);
