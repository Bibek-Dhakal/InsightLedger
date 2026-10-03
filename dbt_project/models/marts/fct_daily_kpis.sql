with orders as (select *
                from {{ ref('stg_ecommerce__orders') }}),
     users as (select *
               from {{ ref('stg_ecommerce__users') }})

select date_trunc('day', order_date) as reporting_date,
       count(distinct user_id)       as purchasing_users,
       count(distinct order_id)      as total_orders,
       sum(amount)                   as total_revenue
from orders
where status = 'completed'
group by 1
