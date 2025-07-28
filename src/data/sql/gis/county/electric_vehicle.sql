SELECT 
    LEFT(geoid::text, 5) as fips, 
    SUM(CASE WHEN year = 2022 THEN bev else 0 END) as bev_2022, 
    SUM(CASE WHEN year = 2023 THEN bev else 0 END) as bev_2023, 
    SUM(CASE WHEN year = 2024 THEN bev else 0 END) as bev_2024 
FROM "31691dde-5bd5-4570-ab9f-79c498f72497" 
where geoid IS NOT NULL 
group by fips