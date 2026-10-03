select user_id,
       signup_date
from {{ source('public_data', 'users') }}
