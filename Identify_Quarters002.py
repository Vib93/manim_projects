from manim import *

class Identify_Quarters002(Scene):
    config.background_color=WHITE
    config.frame_height=10
    config.frame_width=20
    def construct(self):
        self.camera.background_color=WHITE
        self.camera.frame_height=10
        self.camera.frame_width=20
        img=ImageMobject("mainBG.png").scale_to_fit_height(config["frame_height"]).set_opacity(0.8)
        self.add(img)
        top_left=[-2,3,0]
        top_right=[2,3,0]
        bottom_right=[2,1,0]
        bottom_left=[-2,1,0]
        R2=Polygon(top_right,top_left,bottom_left,bottom_right,stroke_color="#ED6CEF",fill_color="#EBBDEC",fill_opacity=1)
        d1=Line(start=top_left,end=bottom_right,stroke_color="#ED6CEF")
        d2=Line(start=top_right,end=bottom_left,stroke_color="#ED6CEF")
        #self.play(FadeIn(R2,d1,d2))
        #self.wait(5)
        text1=Text("1",font_size=18,color=BLACK ,font="Athletics Regular").move_to([0.25,2.75,1])
        text2=Text("2",font_size=18,color=BLACK,font="Athletics Regular").move_to([1.75,1.75,1])
        text3=Text("3",font_size=18,color=BLACK,font="Athletics Regular").move_to([0.25,1.25,1])
        text4=Text("4",font_size=18,color=BLACK,font="Athletics Regular").move_to([-1.75,1.75,1])
        v1=DashedLine(start=[0,3.5,0],end=[0,0.75,0]).set_color("#000000")
        h1=DashedLine(start=[-2.5,2,0],end=[2.5,2,0]).set_color("#000000")
        t1=Polygon(top_left,[0,3,0],[0,2,0]).set_stroke(color="#B038B2",width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        t2=Polygon(top_right,[0,3,0],[0,2,0]).set_stroke(color="#B038B2",width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        text1copy=text1.copy()
        groupt12=Group(t1,t2,text1copy)
        t3=Polygon(top_right,[2,2,0],[0,2,0]).set_stroke(color="#B038B2", width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        t4=Polygon(bottom_right,[2,2,0],[0,2,0]).set_stroke(color="#B038B2",width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        text2copy=text2.copy()
        groupt34=Group(t3,t4,text2copy)
        t5=Polygon(bottom_right,[0,1,0],[0,2,0]).set_stroke(color="#B038B2", width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        t6=Polygon(bottom_left,[0,1,0],[0,2,0]).set_stroke(color="#B038B2", width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        text3copy=text3.copy()
        groupt3=Group(t5,t6,text3copy)
        def alwaysup(mobject,t):
            mobject.rotate(-t*PI)
        t7=Polygon(bottom_left,[-2,2,0],[0,2,0]).set_stroke(color="#B038B2", width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        t8=Polygon(top_left,[-2,2,0],[0,2,0]).set_stroke(color="#B038B2", width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        text4copy=text4.copy()
        groupt4=Group(t7,t8,text4copy)
        
        
        self.play(FadeIn(R2))
        self.play(Create(d1),Create(d2))
        self.play(Create(v1),Create(h1))
        self.play(FadeIn(text1,text2,text3,text4))
        self.wait(1)
        self.play(FadeIn(groupt12))
        self.wait(1)
        self.play(groupt12.animate.move_to([-6,-1,0]))
        self.wait(1)  
        self.play(FadeIn(groupt34))
        self.wait(1)
        self.play(groupt34.animate.move_to([-2.9,-0.50,0]))
        #self.wait(2)
        v=t3.get_vertices()[3]
        self.play(Rotate(t3,angle =-PI,about_point=v,rate_func=linear))
        self.play(FadeIn(groupt3))
        self.play(groupt3.animate.move_to([2.2,-1,0]))
        self.play(Rotate(groupt3,angle=-PI),UpdateFromAlphaFunc(text3copy,alwaysup))
        self.play(FadeIn(groupt4))
        self.play(groupt4.animate.move_to([7.3,-0.5,0]))
        v3=t8.get_vertices()[3]
        self.play(Rotate(t8,angle=PI,about_point=v3))
        self.wait(2)
        groupt12.set_z_index(2)
        self.play(groupt34.animate.move_to([0,-1.5,0]),groupt3.animate.move_to([0,-1.5,0]),groupt4.animate.move_to([0,-1.5,0]),groupt12.animate.move_to([0,-1.5,0]))
        self.wait(5)
        