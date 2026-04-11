from manim import *
import numpy as np

class MultiplicativeInverseGeometry(Scene):
    """
    Visualises alpha = -2 + 2i and its inverse beta = -1/4 - 1/4i
    on the complex plane, showing how the inverse undoes both the
    rotation and the scaling.
    """

    def construct(self):
        # --- complex plane ---
        plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            background_line_style={"stroke_opacity": 0.4},
        )
        self.play(Create(plane), run_time=1.5)

        # --- alpha = -2 + 2i ---
        alpha = complex(-2, 2)
        alpha_point = plane.n2p(alpha)
        alpha_dot = Dot(alpha_point, color=BLUE, radius=0.08)
        alpha_label = Text("a = -2+2i", font_size=20, color=BLUE)
        alpha_label.next_to(alpha_dot, UL, buff=0.15)
        alpha_vec = Arrow(plane.n2p(0), alpha_point, buff=0, color=BLUE, stroke_width=3)

        self.play(GrowArrow(alpha_vec), FadeIn(alpha_dot), Write(alpha_label), run_time=1.5)

        # --- show angle arc for alpha (135 degrees) ---
        alpha_angle = np.arctan2(alpha.imag, alpha.real)  # 3pi/4
        arc_alpha = Arc(
            radius=0.8,
            start_angle=0,
            angle=alpha_angle,
            arc_center=plane.n2p(0),
            color=BLUE,
        )
        angle_label_alpha = Text("135°", font_size=18, color=BLUE)
        angle_label_alpha.move_to(
            plane.n2p(0) + 1.15 * np.array([np.cos(alpha_angle / 2), np.sin(alpha_angle / 2), 0])
        )
        self.play(Create(arc_alpha), Write(angle_label_alpha), run_time=1)

        # --- conjugate: flip across real axis ---
        conj = alpha.conjugate()  # -2 - 2i
        conj_point = plane.n2p(conj)
        conj_dot = Dot(conj_point, color=YELLOW, radius=0.08)
        conj_label = Text("conj(a) = -2-2i", font_size=20, color=YELLOW)
        conj_label.next_to(conj_dot, DL, buff=0.15)
        conj_vec = Arrow(plane.n2p(0), conj_point, buff=0, color=YELLOW, stroke_width=3)

        flip_text = Text("flip across real axis (conjugate)", font_size=22, color=YELLOW)
        flip_text.to_edge(UP)

        self.play(Write(flip_text), run_time=0.8)
        self.play(
            GrowArrow(conj_vec), FadeIn(conj_dot), Write(conj_label), run_time=1.5
        )

        # --- show angle arc for conjugate (-135 degrees) ---
        conj_angle = np.arctan2(conj.imag, conj.real)  # -3pi/4
        arc_conj = Arc(
            radius=0.7,
            start_angle=0,
            angle=conj_angle,
            arc_center=plane.n2p(0),
            color=YELLOW,
        )
        angle_label_conj = Text("-135°", font_size=18, color=YELLOW)
        angle_label_conj.move_to(
            plane.n2p(0) + 1.05 * np.array([np.cos(conj_angle / 2), np.sin(conj_angle / 2), 0])
        )
        self.play(Create(arc_conj), Write(angle_label_conj), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(flip_text), run_time=0.5)

        # --- scale down to get beta = conj / |alpha|^2 ---
        beta = conj / abs(alpha) ** 2  # (-1/4) - (1/4)i
        beta_point = plane.n2p(beta)
        beta_dot = Dot(beta_point, color=GREEN, radius=0.08)
        beta_label = Text(
            "b = conj(a)/|a|² = -1/4 - 1/4 i",
            font_size=16,
            color=GREEN,
        )
        beta_label.next_to(beta_dot, DR, buff=0.15)
        beta_vec = Arrow(plane.n2p(0), beta_point, buff=0, color=GREEN, stroke_width=3)

        scale_text = Text("scale down by |a|² = 8", font_size=22, color=GREEN)
        scale_text.to_edge(UP)

        self.play(Write(scale_text), run_time=0.8)
        self.play(
            Transform(conj_vec.copy(), beta_vec),
            FadeIn(beta_dot),
            Write(beta_label),
            run_time=2,
        )
        self.wait(0.5)
        self.play(FadeOut(scale_text), run_time=0.5)

        # --- show the product: alpha * beta = 1 ---
        product_text = Text(
            "a * b:  +135° + (-135°) = 0°,  2√2 * 1/(2√2) = 1",
            font_size=20,
        )
        product_text.to_edge(UP)

        result_dot = Dot(plane.n2p(1), color=RED, radius=0.1)
        result_label = Text("a * b = 1", font_size=22, color=RED)
        result_label.next_to(result_dot, UR, buff=0.15)
        result_vec = Arrow(plane.n2p(0), plane.n2p(1), buff=0, color=RED, stroke_width=3)

        self.play(Write(product_text), run_time=2)
        self.wait(1)
        self.play(
            GrowArrow(result_vec), FadeIn(result_dot), Write(result_label), run_time=1.5
        )
        self.wait(2)
