-- blog增加格式化后内容和格式化类型字段
alter table blog_blog add column format_body text;
alter table blog_blog add column format_type integer;