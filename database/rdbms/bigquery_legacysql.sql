#legacySQL
SELECT
    weight_punds, state, year, gestation_weeks
FROM
    [bigquery-public-data:samples.natality ]
ORDER BY weight_pounds DESC
LIMIT 10;