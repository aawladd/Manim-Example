
#This Code Will Run in Manimgl
from io import BufferedWriter
from optparse import Values
from tkinter.constants import CENTER
from jedi.inference import value
from manimlib import *
from pyglet.graphics import draw



class Harmonograph(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": BLACK,
     },
    }
    def construct(self):
        #Frequencies
        F1 = 0
        F2 = 0
        F3 = 0
        F4 = 0

        #Phase Shifts 
        P1 = 0
        P2 = 0
        P3 = 0
        P4 = 0

        #Decay Constants

        D1 = 0
        D2 = 0
        D3 = 0
        D4 = 0

        harmonotext = Text("Visualization of Harmonograph")
        harmonotext.scale(1.2)
        harmonotext.set_color(BLUE)
        self.play(Write(harmonotext), run_time = 2)
        self.wait(1)
        eqtext = Text("Parametric Equations")
        eqtext.scale(1.5)
        eqtext.set_color(ORANGE)
        self.play(ReplacementTransform(harmonotext, eqtext))
        self.play(eqtext.to_edge, UP)
        
        equation = VGroup(
        Tex(r"x(t) = e^{-d_{1}t} \sin(f_{1}t + p_{1}) + e^{-d_{2}t} \sin(f_{2}t + p_{2})"),
        Tex(r"y(t) = e^{-d_{3}t} \sin(f_{3}t + p_{3}) + e^{-d_{4}t} \sin(f_{4}t + p_{4})")
        ).arrange(DOWN, aligned_edge = LEFT)
        equation[0].set_color("#00ECFF")
        equation[1].set_color("#55FF00")
        equation.scale(1.2)
        self.play(Write(equation), run_time = 8)
        self.wait(2)

        self.play(FadeOut(eqtext),equation.scale, 0.5, equation.stretch_to_fit_width, 5, equation.to_corner, UR)
        rangee = Tex(r"t\in[0,200]")
        rangee.set_color(ORANGE)
        rangee.next_to(equation, DOWN).align_to(equation, LEFT)
        self.play(Write(rangee))


        valuestext= ["f_{1}","f_{2}","p_{1}", "p_{2}", "d_{1}", "d_{2}","f_{3}","f_{4}","p_{3}", "p_{4}", "d_{3}", "d_{4}"]
        valuescolor = [RED, GREEN, BLUE, ORANGE, YELLOW, GOLD, MAROON, PURPLE, BLUE_A, YELLOW_A, PURPLE_A, GOLD_B]
        values = VGroup(*[
            Tex(f"{t}=").scale(0.5)
            for t in valuestext
        ])
        values[0:6].set_color("#00ECFF")
        values[6:12].set_color("55FF00")

        freq = VGroup(values[0], values[1], values[6], values[7])
        freq.arrange(DOWN,aligned_edge=LEFT,buff=0.5)
        freq.scale(2.5)
        self.play(Write(freq), run_time = 2)
        fq_brac = Brace(freq, LEFT)
        fq_brac_text = fq_brac.get_text("Frequency")
        self.play(GrowFromCenter(fq_brac), Write(fq_brac_text), run_time = 2)
        self.wait()
        freqc = freq.copy()
        freqc.scale(0.6)
        freqc[0].next_to(rangee, DOWN, aligned_edge=LEFT, buff = 0.5)
        freqc[1].next_to(freqc[0], RIGHT, buff = 2.3)
        freqc[2].next_to(freqc[0], DOWN , buff=2.5, aligned_edge=LEFT)
        freqc[3].next_to(freqc[2], RIGHT, buff=2.3)

        phase = VGroup(values[2], values[3], values[8], values[9])
        phase.arrange(DOWN,aligned_edge=LEFT,buff=0.5)
        phase.scale(2.5)
        ph_brac_text = fq_brac.get_text("Phase")
        self.play(ReplacementTransform(fq_brac_text, ph_brac_text),ReplacementTransform(freq, phase), run_time = 3)

        phasec = phase.copy()
        phasec.scale(0.6)
        phasec[0].next_to(freqc[0], DOWN , buff = 0.5, aligned_edge=LEFT)     
        phasec[1].next_to(freqc[1], DOWN , buff = 0.5, aligned_edge=LEFT)     
        phasec[2].next_to(freqc[2], DOWN , buff = 0.5, aligned_edge=LEFT)     
        phasec[3].next_to(freqc[3], DOWN , buff = 0.5, aligned_edge=LEFT)


        damp = VGroup(values[4], values[5], values[10], values[11])
        damp.arrange(DOWN,aligned_edge=LEFT,buff=0.5)
        damp.scale(2.5)
        dm_brac_text = fq_brac.get_text("Damping")
        self.play(ReplacementTransform(ph_brac_text, dm_brac_text),ReplacementTransform(phase, damp), run_time = 3)     
        

        dampc = damp.copy()
        dampc.scale(0.6)
        dampc[0].next_to(phasec[0], DOWN , buff = 0.5, aligned_edge=LEFT)     
        dampc[1].next_to(phasec[1], DOWN , buff = 0.5, aligned_edge=LEFT)     
        dampc[2].next_to(phasec[2], DOWN , buff = 0.5, aligned_edge=LEFT)     
        dampc[3].next_to(phasec[3], DOWN , buff = 0.5, aligned_edge=LEFT)


        self.play(FadeOut(fq_brac), FadeOut(dm_brac_text), FadeOut(damp))
        self.play(Write(freqc), Write(phasec), Write(dampc), run_time = 3)

        xgp = VGroup(freqc[0], phasec[0], dampc[0])
        x_brace = Brace(xgp, LEFT)
        x_brace_text = x_brace.get_text("For x(t)")

        ygp = VGroup(freqc[2], phasec[2], dampc[2])
        y_brace = Brace(ygp, LEFT)
        y_brace_text = y_brace.get_text("For y(t)")

        self.play(GrowFromCenter(x_brace), Write(x_brace_text), GrowFromCenter(y_brace), Write(y_brace_text), run_time = 3)
        self.play(FadeOut(x_brace), FadeOut(y_brace), FadeOut(x_brace_text), FadeOut(y_brace_text))


        #Decimal Numbers
        D_F1 = DecimalNumber(F1)
        D_F2 = DecimalNumber(F2)
        D_F3 = DecimalNumber(F3)
        D_F4 = DecimalNumber(F4)

        D_P1 = DecimalNumber(P1)
        D_P2 = DecimalNumber(P2)
        D_P3 = DecimalNumber(P3)
        D_P4 = DecimalNumber(P4)

        D_D1 = DecimalNumber(D1)
        D_D2 = DecimalNumber(D2)
        D_D3 = DecimalNumber(D3)
        D_D4 = DecimalNumber(D4)

        D_All = VGroup(D_F1, D_F2, D_F3, D_F4, D_P1, D_P2, D_P3, D_P4, D_D1, D_D2, D_D3, D_D4,)
       
        D_F1.next_to(freqc[0], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(RED)
        D_F2.next_to(freqc[1], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(RED)
        D_F3.next_to(freqc[2], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(RED)
        D_F4.next_to(freqc[3], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(RED)

        D_P1.next_to(phasec[0], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(YELLOW)
        D_P2.next_to(phasec[1], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(YELLOW)
        D_P3.next_to(phasec[2], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(YELLOW)
        D_P4.next_to(phasec[3], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(YELLOW)

        D_D1.next_to(dampc[0], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(TEAL)
        D_D2.next_to(dampc[1], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(TEAL)
        D_D3.next_to(dampc[2], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(TEAL)
        D_D4.next_to(dampc[3], aligned_edge=DOWN, buff= 0.05).scale(0.6).set_color(TEAL)

        self.play(Write(D_All))

        pc = self.parametricfunction(F1, F2, F3, F4, P1, P2, P3, P4, D1, D2, D3, D4)
        pc.add_updater(
            lambda mob : mob.become(
                self.parametricfunction(
                    D_F1.get_value(),
                    D_F2.get_value(),
                    D_F3.get_value(),
                    D_F4.get_value(),

                    D_P1.get_value(),
                    D_P2.get_value(),
                    D_P3.get_value(),
                    D_P4.get_value(),

                    D_D1.get_value(),
                    D_D2.get_value(),
                    D_D3.get_value(),
                    D_D4.get_value(),
                )
            ).shift(LEFT*3)
        )
 
        
        self.add(pc)

        self.play(
            ChangeDecimalToValue(D_F1,1),
            ChangeDecimalToValue(D_F2,6),
            ChangeDecimalToValue(D_F3,1),
            ChangeDecimalToValue(D_F4,6),
            ChangeDecimalToValue(D_P1, PI/2),
            ChangeDecimalToValue(D_P2,3 * PI/2),
            ChangeDecimalToValue(D_P3,0),
            ChangeDecimalToValue(D_P4,0),
            ChangeDecimalToValue(D_D1,0.02),
            ChangeDecimalToValue(D_D2,0.02),
            ChangeDecimalToValue(D_D3,0.02),
            ChangeDecimalToValue(D_D4,0.01),
            run_time=15,
            rate_func=linear,
        )
        self.wait(0.5)


        self.play(
            ChangeDecimalToValue(D_F3,4),
            ChangeDecimalToValue(D_P1, PI/16),
            run_time=5,
            rate_func=linear,
        )
        self.wait(0.5)

        self.play(
            ChangeDecimalToValue(D_F2,4),
            run_time=15,
            rate_func=linear,
        )
        self.wait(0.5)

        self.play(
            ChangeDecimalToValue(D_F1,2.7),
            ChangeDecimalToValue(D_F2,6.35),
            ChangeDecimalToValue(D_F3,8.15),
            ChangeDecimalToValue(D_F4,4.55),
            ChangeDecimalToValue(D_P1,4.65),
            ChangeDecimalToValue(D_P2,4.15),
            ChangeDecimalToValue(D_P3,4.4 ),
            ChangeDecimalToValue(D_P4,5.43),
            run_time=15,
            rate_func=linear,
        )
        self.wait(0.5)

        self.play(
            ChangeDecimalToValue(D_F4,0.9),
            run_time=15,
            rate_func=linear,
        )
        self.wait(0.5)

        self.play(
            ChangeDecimalToValue(D_F1,3.65),
            ChangeDecimalToValue(D_F2,7.3),
            ChangeDecimalToValue(D_F3,0.9),
            ChangeDecimalToValue(D_F4,3.65),
            run_time=15,
            rate_func=linear,
        )
        self.wait(0.5)
        self.wait(1)
    def parametricfunction(self, f1, f2, f3, f4, p1, p2, p3, p4, d1, d2, d3, d4):
        tol = 1e-9
        pc = ParametricCurve(
            lambda t: np.array([
               np.exp(-d1*t)*np.sin(f1*t + p1) + np.exp(-d2*t)*np.sin(f2*t + p2),
               np.exp(-d3*t)*np.sin(f3*t + p3) + np.exp(-d4*t)*np.sin(f4*t + p4),
                0
            ]),
            t_range=[0, 200],
            tolerance_for_point_equality=tol,
            epsilon=tol,
            stroke_width = 1
        )
        pc.set_color(color=[RED,YELLOW,BLUE,RED,ORANGE])
        pc.scale(2)
        return pc



         