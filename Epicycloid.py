from manimlib.imports import *



class Introduction(Scene):
    def construct(self):
        text = TexMobject(
            "\\text{Visualization of",
         "Epicycloid}")
        text[1].set_color(BLUE)
        text[0].scale(1.5)
        text[1].scale(2)
        text[1].next_to(text[0], DOWN)
        text.move_to(0.5*RIGHT)
        self.play(Write(text), runt_time = 5)
        self.play(text.scale, 2, runt_time = 3)
        self.play(FadeOut(text), run_time = 2)
    

class EpicycloidSceneComplete(Scene):
    CONFIG = {
            "radius":1.5,
            "color_path":RED,
            "divisions":[1,2,3,4,5,6]
    }
    def construct(self):
        self.show_axes()
        self.show_animation()

    def show_axes(self,partition=3):
        step_size = 2.5/partition
        # See all options in manimlib/mobject/number_line.py
        x_axis = NumberLine(
                x_min = -step_size*7, 
                x_max = step_size*7.8,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=WHITE,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":"#66ff99"}
                )
        y_axis = NumberLine(
                x_min = -step_size*5, 
                x_max = step_size*5.5,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=WHITE,
                label_direction = UP,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":"#66ff99"}
                )
        y_axis.rotate(PI/2,about_point = ORIGIN)
        # rotate labels in y_axis
        for number in y_axis.numbers:
            number.rotate(-PI/2,about_point = number.get_center())

        self.play(Write(x_axis),Write(y_axis))
        self.wait()

    def show_animation(self):
        c = True
        for i in self.divisions:
            self.epy(self.radius,self.radius/i,c)
            c = False
        
    def epy(self,r1,r2,animation):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=YELLOW).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        dot = Dot(c2.point_from_proportion(0),color=self.color_path)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(GREEN,2.5)
        # Path
        path = VMobject(color=self.color_path)
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        # Alpha
        alpha = ValueTracker(0)
        
        # If the animation start then shows the animation
        if animation:
            self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))
        else:
            self.remove(self.dot)
            self.add_foreground_mobjects(dot)
            self.play(ShowCreation(line),ShowCreation(c2))
            self.remove_foreground_mobjects(dot)
            self.add(c1,c2,path)

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.point_from_proportion(0))
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1],dot.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),dot.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU*alpha.get_value(),about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha.get_value(),about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2,path_group)
        self.play(
                alpha.set_value,1,
                rate_func=linear,
                run_time=10
                )
        self.wait()
        c2.clear_updaters()
        path_group.clear_updaters()
        self.dot = dot
        self.play(FadeOut(path),FadeOut(c2),FadeOut(line))
