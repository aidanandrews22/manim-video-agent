from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SolvingQuadraticEquation(VoiceoverScene):
    def construct(self):
        # Set up the voiceover service
        self.set_speech_service(GTTSService())
        
        # Configure visual style based on the animation plan
        self.camera.background_color = "#1C1C1C"
        accent_color = "#3B82F6"
        
        # Section 1: Introduction to Quadratic Equations
        with self.voiceover("""
            Welcome to our exploration of quadratic equations! Today, we're diving into the equation 
            x squared minus 5x plus 6 equals zero.
        """):
            title = MathTex(r"x^2 - 5x + 6 = 0", color=WHITE).scale(1.5)
            self.play(FadeIn(title))
        
        with self.voiceover("""
            This is a classic example of a quadratic equation, which generally takes the form 
            ax squared plus bx plus c equals zero. Let's break it down together.
        """):
            general_form = MathTex(r"ax^2 + bx + c = 0", color=WHITE).scale(1.5)
            self.play(FadeIn(general_form))
            self.wait(0.5)
            self.play(FadeOut(title), FadeOut(general_form))
        
        # Section 2: Recognizing the Form
        with self.voiceover("""
            Now, let's identify the key components of our equation.
        """):
            equation = MathTex(r"x^2 - 5x + 6 = 0", color=WHITE).scale(1.2)
            self.play(FadeIn(equation))
        
        with self.voiceover("""
            Here, the coefficient a is 1, b is negative 5, and c is 6. 
            Recognizing these values is crucial as they guide us in solving the equation.
        """):
            coefficients = MathTex(r"a = 1, \quad b = -5, \quad c = 6", color=accent_color).scale(1.2)
            self.play(Transform(equation, coefficients))
            self.wait(0.5)
        
        # Section 3: Factoring the Quadratic
        with self.voiceover("""
            Next, we'll factor the quadratic equation.
        """):
            self.play(FadeOut(equation))
            original_equation = MathTex(r"x^2 - 5x + 6 = 0", color=WHITE).scale(1.2)
            self.play(FadeIn(original_equation))
        
        with self.voiceover("""
            We're looking for two numbers that multiply to 6 and add up to 5.
        """):
            condition = MathTex(r"r \times s = 6 \quad \text{and} \quad r + s = 5", color=WHITE).scale(1.2)
            self.play(Write(condition))
            self.play(original_equation.animate.shift(UP*1.5), condition.animate.shift(DOWN*0.5))
        
        with self.voiceover("""
            These numbers are 2 and 3.
        """):
            numbers = MathTex(r"r = 2, \quad s = 3", color=accent_color).scale(1.2)
            self.play(FadeIn(numbers))
            self.play(numbers.animate.next_to(condition, DOWN, buff=0.5))
        
        with self.voiceover("""
            Thus, we can express the quadratic as x minus 2 times x minus 3. 
            This step is essential for finding the solutions.
        """):
            factored = MathTex(r"(x - 2)(x - 3) = 0", color=WHITE).scale(1.2)
            self.play(Transform(original_equation, factored))
            self.play(FadeOut(condition), FadeOut(numbers))
            self.play(original_equation.animate.move_to(ORIGIN))
        
        # Section 4: Solving for x
        with self.voiceover("""
            With our factors in place, we apply the Zero Product Property.
        """):
            zero_product = MathTex(r"(x - 2)(x - 3) = 0", color=WHITE).scale(1.2)
            self.play(FadeIn(zero_product))
            self.play(FadeOut(original_equation))
        
        with self.voiceover("""
            This means setting each factor equal to zero.
        """):
            factors_zero = MathTex(r"x - 2 = 0 \quad \text{or} \quad x - 3 = 0", color=WHITE).scale(1.2)
            self.play(Transform(zero_product, factors_zero))
        
        with self.voiceover("""
            Solving these gives us the solutions: x equals 2 and x equals 3.
        """):
            solutions = MathTex(r"x = 2, \quad x = 3", color=accent_color).scale(1.5)
            self.play(FadeIn(solutions))
            self.play(solutions.animate.next_to(zero_product, DOWN, buff=0.7))
            self.wait(0.5)
            self.play(FadeOut(zero_product), FadeOut(solutions))
        
        # Section 5: Conclusion and Importance
        with self.voiceover("""
            Let's wrap up by considering the broader significance of quadratic equations.
        """):
            self.wait(0.5)
        
        with self.voiceover("""
            These equations are fundamental in various fields such as mathematics, physics, 
            engineering, and economics. Understanding how to solve them is a valuable skill 
            that opens doors to deeper insights in these areas.
        """):
            importance = Text("Quadratic equations are essential in various fields.", 
                             color=WHITE).scale(0.8)
            self.play(FadeIn(importance))
            self.wait(1)
            self.play(FadeOut(importance))
        
        # Section 6: Example Problem
        with self.voiceover("""
            To reinforce what we've learned, let's tackle another example.
        """):
            self.wait(0.5)
        
        with self.voiceover("""
            Consider the quadratic equation x squared minus 9x plus 18 equals zero.
        """):
            example = MathTex(r"x^2 - 9x + 18 = 0", color=WHITE).scale(1.2)
            self.play(FadeIn(example))
        
        with self.voiceover("""
            Factoring gives us x minus 3 times x minus 6 equals zero.
        """):
            factored_example = MathTex(r"(x - 3)(x - 6) = 0", color=WHITE).scale(1.2)
            self.play(Transform(example, factored_example))
        
        with self.voiceover("""
            Solving these factors, we find the solutions: x equals 3 and x equals 6. 
            Practice like this solidifies your understanding and prepares you for more complex problems.
        """):
            example_solutions = MathTex(r"x = 3, \quad x = 6", color=accent_color).scale(1.5)
            self.play(FadeIn(example_solutions))
            self.play(example_solutions.animate.next_to(example, DOWN, buff=0.7))
            self.wait(1)
            
            # Final fade out
            self.play(FadeOut(example), FadeOut(example_solutions))
            
            # Display a concluding message
            conclusion = Text("Thank you for watching!", color=WHITE).scale(1.2)
            self.play(FadeIn(conclusion))
            self.wait(2)
