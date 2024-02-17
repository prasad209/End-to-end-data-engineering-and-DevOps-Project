{% set film_title = 'Dunkirk' %}

select * from  {{ref("films")}}
where title = '{{film_title}}'