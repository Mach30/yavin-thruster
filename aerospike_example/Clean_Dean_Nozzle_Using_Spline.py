import cadquery as cq
from Helpers import show

# Attributes we can modify
scale = 0.125                 # The scale in relation to normal size (% / 100)
rgba = (204, 204, 204, 0.0)   # The color and transparency of the model

# The points for the outline of the spike
spike_points = [
    (7.31058536987926, 11.0165328678702),
    (7.29209592126546, 11.0270071060423),
    (7.27238894084329, 11.039277065777),
    (7.25129565196959, 11.0536201349458),
    (7.22864456252685, 11.0703473914655),
    (7.20425764118421, 11.0898088975634),
    (7.17794732182628, 11.1123994657636),
    (7.14951394663526, 11.1385650784009),
    (7.11874341758329, 11.1688101281429),
    (7.08540490883067, 11.2037056523581),
    (7.04924853649798, 11.243898752355),
    (7.0100029052478, 11.2901234170726),
    (6.96737246182478, 11.3432130094645),
    (6.92103458858197, 11.4041147236265),
    (6.87063636726188, 11.473906383781),
    (6.81579093586704, 11.5538160356454),
    (6.7560733495435, 11.6452448807842),
    (6.69101583966025, 11.749794231057),
    (6.6201023428587, 11.8692973209945),
    (6.5427621424216, 12.0058570212954),
    (6.45836242590977, 12.1618907607559),
    (6.3661995128761, 12.3401843060196),
    (6.26548844074251, 12.5439564949569),
    (6.1553505102395, 12.7769376068103),
    (6.03479827661213, 13.0434648316541),
    (5.90271731838607, 13.3485993456133),
    (5.75784390653807, 13.6982709102955),
    (5.59873741121177, 14.099457845082),
    (5.42374588805677, 14.5604128895892),
    (5.23096273330545, 15.0909492085831),
    (5.01817151248803, 15.7028060883286),
    (4.78277493953884, 16.4101214927169),
    (4.52170233477736, 17.230049779283),
    (4.23128744096091, 18.1835794158505),
    (3.90710476888003, 19.2966305755316),
    (3.54374691517922, 20.6015511662541),
    (3.13451623969209, 22.1391909699118),
    (2.67098960228534, 23.9618326248229),
    (2.14239030043114, 26.1374234847559),
    (1.53465850644412, 28.7558385724394),
    (0.829027589566102, 31.9384397404038),
    (0, 35.8524021267837)
]

# The points defining the combustion chamber outline
chamber_points = [
    (8.5868, 0),
    (8.5868, 7.7),
    (8.0868, 8.8),
    (8.0868, 9.9),
    (7.5868, 11),
    (7.5868, 11.73589),
    (7.8966, 11.73589),
    (7.8966, 11),
    (8.3989, 9.9),
    (8.9071, 8.8),
    (8.9071, 0),
    (8.5868, 0)
]

# Points defining the outline of the injector plate
injector_points = (
    (7.1139, 0),
    (8.9159, 0),
    (8.9159, -2),
    (7.1139, -2),
    (7.1139, 0)
)

# Scale our points to 1/8 normal size
spike_points_scaled = [(x * scale, y * scale) for x, y in spike_points]
chamber_points_scaled = [(x * scale, y * scale) for x, y in chamber_points]
injector_points_scaled = [(x * scale, y * scale) for x, y in injector_points]

# Figure out our start points for the spike (compensates for scaling)
spike_start_x = 7.32802871061466 * scale
spike_start_y = 11.007605598221 * scale

spike = cq.Workplane('XZ').moveTo(spike_start_x, spike_start_y)\
                          .spline(spike_points_scaled)\
                          .lineTo(0.0 * scale, 11.007605598221 * scale)\
                          .close()
chamber = cq.Workplane('XZ').polyline(chamber_points_scaled)
injector = cq.Workplane('XZ').polyline(injector_points_scaled)

spike = spike.revolve()
chamber = chamber.revolve()
injector = injector.revolve()

# Use the following to render your model with grey RGB and no transparency
show(spike, rgba)
show(chamber, rgba)
show(injector, rgba)
