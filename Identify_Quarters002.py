from manim import *

class Identify_Quarters002(Scene):
    def construct(self):
        self.camera.background_color = "#8DD5F1"  
        top_left=[-2,3,0]
        top_right=[2,3,0]
        bottom_right=[2,1,0]
        bottom_left=[-2,1,0]
        R2=Polygon(top_right,top_left,bottom_left,bottom_right,stroke_color="#ED6CEF",fill_color="#EBBDEC",fill_opacity=1)
        d1=Line(start=top_left,end=bottom_right,stroke_color="#ED6CEF")
        d2=Line(start=top_right,end=bottom_left,stroke_color="#ED6CEF")
        #self.play(FadeIn(R2,d1,d2))
        #self.wait(5)
        text1=Text("1",font_size=18,color=BLACK).move_to([0.25,2.75,1])
        text2=Text("2",font_size=18,color=BLACK).move_to([1.75,2.25,1])
        text3=Text("3",font_size=18,color=BLACK).move_to([0.25,1.25,1])
        text4=Text("4",font_size=18,color=BLACK).move_to([-1.75,2.25,1])
        v1=Line(start=[0,5,0],end=[0,0,0]).set_color("#ED6CEF")
        h1=Line(start=[-3,2,0],end=[3,2,0]).set_color("#ED6CEF")
        group_original= Group(R2)
        self.play(FadeIn(group_original))
        self.play(Create(d1),Create(d2))
        self.play(Create(v1),Create(h1))
        #group_original.add(d1,d2)
        self.play(FadeIn(text1,text2,text3,text4))
        self.wait(2)
        
       
        self.wait(2)
        group_original.add(v1,h1)
        t1=Polygon(top_left,[0,3,0],[0,2,0]).set_stroke(color="#B038B2",width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        t2=Polygon(top_right,[0,3,0],[0,2,0]).set_stroke(color="#B038B2",width=3).round_corners(radius=0.001).set_fill(color="#850F85",opacity=1)
        text1copy=text1.copy()
        groupt12=Group(t1,t2,text1copy)
        self.play(FadeIn(groupt12))
        self.wait(2)
        self.play(groupt12.animate.move_to([-3,-2,0]))
        self.wait(2)
        t3=Polygon(top_right,[2,2,0],[0,2,0]).set_stroke(color="#B038B2", width=3).set_fill(color="#850F85",opacity=1)
        t3copy=t3.copy().set_opacity(0)
        t3.round_corners(radius=0.001)
        t4=Polygon(bottom_right,[2,2,0],[0,2,0]).set_stroke(color="#B038B2",width=3).set_fill(color="#850F85",opacity=1).round_corners(radius=0.001)
        text2copy=text2.copy().move_to[]
        groupt34=Group(t3,t4,t3copy,text2copy)
        #border2_t3 = t3.copy().set_stroke(color=YELLOW, width=5).round_corners(radius=0.001)
        #border2_t4 = t4.copy().set_stroke(color=YELLOW,width =5).round_corners(radius=0.001)
        self.play(FadeIn(groupt34))
        self.wait(1)
        self.play(groupt34.animate.move_to([2,-1,0]))
        self.wait(2)
        #t3copy.move_to([2,-1,0])
        v=t3copy.get_vertices()[1]
        self.play(Rotate(t3,angle =-PI,about_point=v,rate_func=linear))
        self.play(groupt34.animate.move_to([3,0,0]))

        self.wait(5)