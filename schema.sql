
drop table if exists tags;
create table tags (
  tag_id integer primary key autoincrement,
  tag_name text not null
);

drop table if exists markpage;
create table markpage (
  page_id integer primary key autoincrement,
  tag_id integer not null,
  title text not null,
  weblink text not null,
  pub_date integer
);

