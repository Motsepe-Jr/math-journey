# Manim animation: Secant lines approaching tangent line
# Run with: manim -pql secant_animation.py SecantToTangent

from manim import *

class SecantToTangent(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-0.5, 3, 0.5],
            y_range=[-0.5, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True}
        )
        
        # Parabola y = x^2
        parabola = axes.plot(lambda x: x**2, x_range=[0, 2.2], color=BLUE)
        parabola_label = MathTex("y = x^2").next_to(parabola, RIGHT)
        
        # Point P
        P = axes.c2p(1, 1)
        P_dot = Dot(P, color=RED)
        P_label = MathTex("P(1,1)").next_to(P_dot, DOWN+LEFT)
        
        # Tangent line y = 2x - 1
        tangent = axes.plot(lambda x: 2*x - 1, x_range=[0, 2.5], color=GREEN)
        tangent_label = MathTex("y = 2x - 1", color=GREEN).to_corner(UR)
        
        self.play(Create(axes), Create(parabola), Write(parabola_label))
        self.play(Create(P_dot), Write(P_label))
        self.wait()
        
        # Animate secant lines for different Q positions
        x_values = [2.5, 2.0, 1.5, 1.3, 1.2, 1.1, 1.05]
        
        Q_dot = None
        secant_line = None
        slope_text = None
        Q_label = None
        
        for i, x_q in enumerate(x_values):
            y_q = x_q**2
            Q = axes.c2p(x_q, y_q)
            new_Q_dot = Dot(Q, color=YELLOW)
            new_Q_label = MathTex(f"Q({x_q:.2f}, {y_q:.2f})").next_to(new_Q_dot, UP+RIGHT, buff=0.1).scale(0.7)
            
            # Calculate slope
            slope = (y_q - 1) / (x_q - 1)
            
            # Create secant line
            new_secant = axes.plot(
                lambda x, s=slope: 1 + s*(x - 1),
                x_range=[0, 2.5],
                color=ORANGE
            )
            
            new_slope_text = MathTex(f"m_{{PQ}} = {slope:.2f}").to_corner(UL)
            
            if i == 0:
                self.play(
                    Create(new_Q_dot),
                    Write(new_Q_label),
                    Create(new_secant),
                    Write(new_slope_text)
                )
                Q_dot = new_Q_dot
                Q_label = new_Q_label
                secant_line = new_secant
                slope_text = new_slope_text
            else:
                self.play(
                    Transform(Q_dot, new_Q_dot),
                    Transform(Q_label, new_Q_label),
                    Transform(secant_line, new_secant),
                    Transform(slope_text, new_slope_text),
                    run_time=0.8
                )
            
            self.wait(0.3)
        
        # Show tangent line
        self.play(
            Create(tangent),
            Write(tangent_label),
            FadeOut(Q_dot),
            FadeOut(Q_label),
            FadeOut(secant_line)
        )
        
        final_text = MathTex(r"\lim_{x \to 1} m_{PQ} = 2").to_corner(UL)
        self.play(Transform(slope_text, final_text))
        self.wait(2)


class VelocityProblem(Scene):
    """Animation showing average velocity approaching instantaneous velocity"""
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 150, 25],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True}
        )
        
        x_label = axes.get_x_axis_label("t")
        y_label = axes.get_y_axis_label("s(t)")
        
        # Distance function s(t) = 4.9t^2
        distance_curve = axes.plot(lambda t: 4.9 * t**2, x_range=[0, 5.5], color=BLUE)
        curve_label = MathTex("s(t) = 4.9t^2").next_to(distance_curve, RIGHT)
        
        # Point P at t=5
        P = axes.c2p(5, 4.9 * 25)
        P_dot = Dot(P, color=RED)
        P_label = MathTex("P(5, 122.5)").next_to(P_dot, DOWN)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(distance_curve), Write(curve_label))
        self.play(Create(P_dot), Write(P_label))
        self.wait()
        
        # Title
        title = Text("Average Velocity → Instantaneous Velocity", font_size=30).to_edge(UP)
        self.play(Write(title))
        
        # Animate secant lines for shrinking intervals
        h_values = [2, 1, 0.5, 0.2, 0.1]
        
        for i, h in enumerate(h_values):
            t_q = 5 + h
            s_q = 4.9 * t_q**2
            Q = axes.c2p(t_q, s_q)
            Q_dot = Dot(Q, color=YELLOW)
            
            # Average velocity
            avg_vel = (s_q - 122.5) / h
            
            # Secant line
            slope = avg_vel
            secant = axes.plot(
                lambda x, s=slope: 122.5 + s * (x - 5),
                x_range=[3, 7],
                color=ORANGE
            )
            
            vel_text = MathTex(f"h = {h}, \\quad v_{{avg}} = {avg_vel:.2f} \\text{{ m/s}}").to_corner(UL)
            
            if i == 0:
                self.play(Create(Q_dot), Create(secant), Write(vel_text))
                current_Q = Q_dot
                current_secant = secant
                current_text = vel_text
            else:
                new_Q = Dot(Q, color=YELLOW)
                self.play(
                    Transform(current_Q, new_Q),
                    Transform(current_secant, secant),
                    Transform(current_text, vel_text),
                    run_time=0.8
                )
            self.wait(0.5)
        
        # Show tangent (instantaneous velocity)
        tangent = axes.plot(lambda x: 122.5 + 49 * (x - 5), x_range=[3, 7], color=GREEN)
        final_text = MathTex(r"v_{inst} = \lim_{h \to 0} \frac{s(5+h) - s(5)}{h} = 49 \text{ m/s}").to_corner(UL)
        
        self.play(
            Transform(current_secant, tangent),
            Transform(current_text, final_text),
            FadeOut(current_Q)
        )
        self.wait(2)
