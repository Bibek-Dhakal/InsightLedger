select user_id,
       variant,
       converted
from {{ source('public_data', 'experiments') }}
