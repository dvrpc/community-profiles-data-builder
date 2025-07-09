SELECT
  c.fips,

  -- Miles of existing trails

  COALESCE((
    SELECT (SUM(ST_Length(ST_Intersection(c.shape, t.shape))) / 1609.34)
    FROM transportation.all_trails t
    WHERE ST_Intersects(c.shape, t.shape)
  ), 0) AS existing_trail_mi,

  -- Miles of circuit trails that are planned, in pipeline, or in progress

  COALESCE((
    SELECT (SUM(ST_Length(ST_Intersection(c.shape, ct.shape))) / 1609.34)
    FROM transportation.circuittrails ct
    WHERE ST_Intersects(c.shape, ct.shape) and ct.circuit != 'Existing'
  ), 0) AS planned_trail_mi,

  -- Miles of freight rail
  
  COALESCE((
    SELECT (SUM(ST_Length(ST_Intersection(c.shape, fr.shape))) / 1609.34)
    FROM freight.freight_rail fr
    WHERE ST_Intersects(c.shape, fr.shape)
  ), 0) AS freight_rail_mi,

  -- Miles of highway

  COALESCE((
    SELECT (SUM(ST_Length(ST_Intersection(c.shape, hw.shape))) / 1609.34)
    FROM freight.highways hw
    WHERE ST_Intersects(c.shape, hw.shape)
  ), 0) AS highway_mi,

  COALESCE((
    SELECT (SUM(ST_Area(ST_Intersection(c.shape, os.shape))) / 1609.34)
    FROM planning.dvrpc_protectedopenspace os
    WHERE ST_Intersects(c.shape, os.shape)
  ), 0) AS protected_open_space_sq_mi
FROM
  boundaries.countyboundaries c
where c.dvrpc_reg = 'Yes';