from manimlib.imports import *

def rate_fun(t):
    if t < 0.5:
        return linear(t*2)
    else:
        return linear(1-(t-0.5)*2)

class ColorValueTracker(Scene):
    def construct(self):
        color_rectangle = Rectangle(
                                    width=FRAME_WIDTH-1,
                                    height=1,
                                    fill_opacity=1,
                                    # Gradient direction
                                    sheen_direction=RIGHT,
                                    stroke_width=0,)
        
        circle = Circle(radius = 0.4, fill_opacity = 1)
        circle.to_edge(UP, buff = 1)
        color_rectangle.to_edge(DOWN, buff=1)
        
        color_rectangle.set_color(color=self.get_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(), unit = "^\\circ")
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(circle,UP))

        circle.add_updater(lambda t: t.set_color(Color(hsl = (color_tracker.get_value()/360, 1, 0.5))))

        line_color = Line(
                        color_rectangle.get_corner(UL),
                        color_rectangle.get_corner(UR),
                        thickness= 2
                        )
        arrow = Arrow(LEFT,RIGHT + UP)
        arrow.add_updater(lambda u: u.put_start_and_end_on(circle.get_bottom() + 0.1 * DOWN,line_color.point_from_proportion(color_tracker.get_value()/360)))

        group = VGroup(color_rectangle, circle, color_label, line_color, arrow)
        self.play(DrawBorderThenFill(group), run_time = 5)
        self.play(
            color_tracker.set_value,360,
            rate_func= rate_fun,
            run_time = 40,
            )
        self.wait(1)
    def get_colors(self, sat = 1, light = 0.5):
        return [*[Color(hsl = (i/360, sat, light)) for i in range(360)]]