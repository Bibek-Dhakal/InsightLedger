select order_id,
       user_id,
       order_date,
       amount,
       status
from {{ source('public_data', 'orders') }}
