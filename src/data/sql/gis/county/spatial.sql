SELECT
  c.fips,
  c.co_name,

  -- Miles of existing trails

  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, t.shape))) / 1609.34)
  --   FROM transportation.all_trails t
  --   WHERE ST_Intersects(c.shape, t.shape)
  -- ), 0) AS existing_trail_mi,


  -- -- Miles of circuit trails that are planned, in pipeline, or in progress

  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, ct.shape))) / 1609.34)
  --   FROM transportation.circuittrails ct
  --   WHERE ST_Intersects(c.shape, ct.shape) and ct.circuit != 'Existing'
  -- ), 0) AS planned_trail_mi,


  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, lts.shape))) / 1609.34)
  --   FROM transportation.lts_network_v2 lts
  --   WHERE ST_Intersects(c.shape, lts.shape) and lts.lts <= 2
  -- ), 0) AS low_stress,

  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, lts.shape))) / 1609.34)
  --   FROM transportation.lts_network_v2 lts
  --   WHERE ST_Intersects(c.shape, lts.shape) and lts.lts > 2
  -- ), 0) AS high_stress,

  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, pn.shape))) / 1609.34)
  --   FROM transportation.pedestriannetwork_lines pn
  --   WHERE ST_Intersects(c.shape, pn.shape)
  -- ), 0) AS pedestrian_network_mi,

  -- -- Miles of freight rail
  
  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, fr.shape))) / 1609.34)
  --   FROM freight.freight_rail fr
  --   WHERE ST_Intersects(c.shape, fr.shape)
  -- ), 0) AS freight_rail_mi,

  -- -- Miles of highway

  -- COALESCE((
  --   SELECT (SUM(ST_Length(ST_Intersection(c.shape, hw.shape))) / 1609.34)
  --   FROM freight.highways hw
  --   WHERE ST_Intersects(c.shape, hw.shape)
  -- ), 0) AS highway_mi,


  -- -- Number of freight centers 

  -- COALESCE((
  --   SELECT COUNT(*)
  --   FROM freight.freight_centers fc
  --   WHERE ST_Area(ST_Intersection(c.shape, fc.shape)) > 0
  -- ), 0) AS unique_freight_centers,

  COALESCE((
    SELECT COUNT(*)
    FROM transportation.patip_fy2025_2028_line tip
    WHERE ST_Intersects(c.shape, tip.shape)
  ), 0) AS fy25_pa_lines,

    COALESCE((
    SELECT COUNT(*)
    FROM transportation.njtip_fy2026_2029_line tip
    WHERE ST_Intersects(c.shape, tip.shape)
  ), 0) AS fy26_nj_lines,

  COALESCE((
    SELECT COUNT(*)
    FROM transportation.patip_fy2025_2028_point tip
    WHERE ST_Intersects(c.shape, tip.shape)
  ), 0) AS fy25_pa_points,

  COALESCE((
    SELECT COUNT(*)
    FROM transportation.njtip_fy2026_2029_point tip
    WHERE ST_Intersects(c.shape, tip.shape)
  ), 0) AS fy26_nj_points

  -- COALESCE((
  --   SELECT (SUM(ST_Area(ST_Intersection(c.shape, os.shape))) / 1609.34)
  --   FROM planning.dvrpc_protectedopenspace os
  --   WHERE ST_Intersects(c.shape, os.shape)
  -- ), 0) AS protected_open_space_sq_mi
FROM
  boundaries.countyboundaries c
where c.dvrpc_reg = 'Yes';