1 About Jing Xiao 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Initial Interest in Computing & Robotics and University of Michigan 4.3 Doctoral Thesis: Problem of Pegging and Hole 4.4 Collaboration at Graduate School 4.5 Seeing the Potential of Robotics: Personal Robots 4.6 Work at Ford, Stanford University and National Science Foundation 4.7 Human Augmentation Elements in Medical Robotics 4.8 Developing Real Time Motion Planning Algorithms 4.9 Work in Haptics 4.10 Challenges of Continuous Manipulator: Deformity and Degrees of Freedom 4.11 Designing Elephant Trunk Robot 4.12 Collaborations 4.13 Challenges to Developing the Robotics Field 4.14 Sources for Grants and Research 4.15 Women in Robotics 4.16 Robotics in China 4.17 Robotics Program at University of North Carolina at Charlotte 4.18 Advice for Prospective Students 4.19 Involvement with the IEEE and the Robotics Automation Society 

## About Jing Xiao

Jing Xiao was born in Beijing, China and received her undergraduate degree at Beijing Normal University. As an undergraduate, Xiao studied physics, electrical engineering, and then migrated to computer engineering and computer science. From there, Xiao went on to University of Michigan for her Master’s and Doctorate degree in Computer Information and Control Engineering. For her Doctorate Thesis, Xiao focused on the problem of pegging and holes, where the challenge was to have a simple robot that can perform only one task, and reason through when encountering errors. After finishing her work at Michigan, Xiao did work on optimizing assembly sequencing, and problem of planning robot motion interaction. In 1998, Dr. Xiao became the program director of the robotics and human augmentation program at the National Science Foundation where she was exposed to the whole landscape of the robotics research. This was where she saw the robotics had the potential to be pervasive as personal computers in our society. After leaving the National Science Foundation and coming back to UNC. Xiao did work on moving the robot around in a dynamic environment, focusing especially on robots with high degree of freedom, and building algorithms that can be developed in real time. 

In this interview, Dr. Xiao talks about her education, how she became interested in robotics, her developing research interests, her collaboration with colleagues and students, and the questions and challenges in moving the robotics field forward. She also touches on issues of diversity in the robotics field, robotics in China, and gives advice to students who may be interested in pursuing robotics. 

## About the Interview

Jing Xiao: An interview conducted by Selma Šabanović, 22 January 2015 

Interview # 799 for Indiana University and the IEEE History Center, The Institute of Electrical and Electronics Engineers, Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Šabanović, [email]. 

It is recommended that this oral history be cited as follows: 

Jing Xiao, an oral history conducted in 2015 by Selma Šabanović, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Jing Xiao 

INTERVIEWER: Selma Šabanović 

DATE: 22 January 2015 

PLACE: College Station, Texas 

### Early Life and Education

Q: <inaudible> ask. So if you could, just start by telling us your name and where you were born. 

Jing Xiao: 

Oh, yeah. I am Jing Xiao. I was born in Beijing, China. I came to U.S. long time ago and studied at the University of Michigan and I received my masters and PhDs from University of Michigan in the program called Computer Information and Control Engineering. It’s an interdisciplinary program. Before that my background was more in physics and electrical engineering. Little bit of a computer science because I was fascinated by computers. So got into more and more in the computer science, now I’m a computer science professor. 

Interviewer: 

Where did you do your undergraduate work? 

Jing Xiao: 

The physics. 

Interviewer: 

In physics. At Michigan as well? 

Jing Xiao: 

No, in China. 

Interviewer: 

In China? What university? 

Jing Xiao: 

It’s Beijing Normal University. It’s-- I entered the physics department then later on, after two years of physics, we got into more electrical engineering. Then kind of migrate from the analog to digital circuits and the computer engineering, then computer science. Computers science is more I learn from Michigan mostly. 

### Initial Interest in Computing & Robotics and University of Michigan

Interviewer: 

What got you interested in computing and robotics? 

Jing Xiao: 

Oh, computing is definitely fascinating because you try to get the machine to process something sophisticated. And I was also interested in the other aspect that we see more of computing, is interface and also graphics interface and simulation. So even when I was an undergraduate student, at the end, I had a project and I did a simulation. At the time, it was just the first or second generation of Apple computer but you can do some graphics work. So I did a simulation of a physics experiment, and you had to program the actual simulation and the graphics display. So that was fascinating to me. Robotics, yeah, I entered-- well, I wasn’t sure what I was going to do but something, anything, to do with some kind of artificial intelligence or robotics sounds good. So I guess that’s how I got into robotics. I could have done database because I worked with a professor and there was some theoretical database aspect, and he thought I could really make some contribution. But as soon as there’s this advertisement for students in robotics, I got excited. That’s how I got into it. 

Interviewer: 

Was there a bunch going on in China before you left for grad school with regards to artificial intelligence and robotics? 

Jing Xiao: 

No, not that I know of. Not much. 

Interviewer: 

So you knew that you wanted to go to study in the states at that time? How did you decide on Michigan? 

<crew talk> 

Jing Xiao: 

Lot of things are accidental, I would say. I didn’t really put a lot of thoughts on certain actions or certain decisions. At the time, that was way prior to the internet era so it’s not easy to get information. I knew somebody in Michigan and also University of Michigan had traditionally a big presence in China, back into the 1930s/1920s. And there’s a-- for example, the first Chinese woman president of a university is from Michigan. So Michigan was quite well-known in China. That’s, I guess, one big reason and I also happened to know somebody. I had an English teacher. She was a student in China and she came from the U.S. and become a foreign student in China for studying Chinese history and so on. And she was from Michigan as well. So a lot of multiple connections I guess. 

Interviewer: 

I see. 

Jing Xiao: 

Yeah, it’s not like I searched through all the universities and tried to find which one fits me. No, it was before that kind of possibility. 

### Doctoral Thesis: Problem of Pegging and Hole

Interviewer: 

What was the first robotics project that you worked on? 

Jing Xiao: 

Well, I worked with Professor Dick Voltz and he actually happened to come back to come to this university later on. But I got my PhD from Michigan, and he presented me this problem of pegging and hole. So this has very tight tolerance and assembly will make you a very simple motion fail. So it becomes a challenging problem and we want the robot, not just some-- a-- how do I say? It’s just a machine that can do only one thing and do one motion but it has to be able to reason when something goes wrong. So we need more intelligent program, more planning whatever, into that robot. It will be able to tackle uncertainty. That’s a hard problem so... 

Interviewer: 

Did that develop into your PhD <inaudible>? 

Jing Xiao: 

PhD, right. Yeah, and, to this day, I don’t think the robotics assembly problem is solved. It’s a long-standing, hard problem. We’ve made progress of course, particularly in more domain-specific situations. You just want to do this type of assembly, you can figure out some way of getting done. But general purpose robot to do assembly, that’s too general purpose assembly. That’s not yet accomplished. 

Interviewer: 

So because there’s so many ways for things to go wrong? 

Jing Xiao: 

Yeah, so many ways for things to go wrong. There’s too much uncertainty and you have to really take into account those uncertainty and lot of times you cannot model the uncertainty beforehand. You have to learn about the uncertainty. So learning approach can work in assembly cases. Yeah, some assembly cases. But the problem with that is you learn the generalization, whether you learn is easily transferable to a different situation. So I think a combination of learning and model-based approach is still the most promising. 

Interviewer: 

What was your thesis title? Do you remember? <inaudible> I don’t remember mine either. 

Jing Xiao: 

I don’t remember it. Something about uncertainty in fine motion planning. 

### Collaboration at Graduate School

Interviewer: 

Okay, and where there any other graduate students that you worked with at Michigan during that time or other faculty you collaborated with? 

Jing Xiao: 

Yeah, as I said, my advisor was Dick Voltz. He passed away actually in 2013. In the little group, or the lab, we had students working different aspects of the problem. One student used to work on assembly sequence planning. Where it’s, if you have a complex assembly, some product, and you-- how that is assembled and follow what sequence, can we automatically decide this kind of sequence? And one student-- so this is-- this student graduated before me and another student graduated before me was also tackling assembly a bit more from the point of view of sensing, force sensing. How to do recognition of different interaction states from force sensing, taking to account uncertainty. 

### Seeing the Potential of Robotics: Personal Robots

Interviewer: 

Where did you go after you finished your work at Michigan? 

Jing Xiao: 

Oh, then I came to where I am now, University of North Carolina at Charlotte. Actually, at the time of graduation, robotics was in a very bad shape. The initial euphoria was faded and people realized there were a lot of tough problems. So-- and there was not many-- how do you say? There were not many places that need or demand people with robotics research background. So it was kind of hard. But anyway, I came to University of North Carolina Charlotte Computer Science Department and I have been there for a few years. And then I went to Ford Research Lab and to have some sabbatical experience and worked on actually assembly lines sequencing optimization. Has nothing to do with robot but it has something to do with assembly. And then I also-- I was at the Stanford University for half a year, visiting and working on the problem of planning robot motion interaction, constrained by contacts and also take advantage of contacts. And after that, I became the program director of the human-- 

<speaker restarts answer> 

Jing Xiao: 

I became the program director of the robotics and human augmentation program at National Science Foundation. And that was a really phenomenal experience because, before that, I was kind of just focused on the little thing and I had been studying and becoming the program director really opened my eyes to the whole landscape of the robotics research. And I realized then that robotics has great potential to be pervasive in society as personal computers. And so we had the initiative that I advocated, personal robotics. I don’t think this term was used for long but we do see a lot of different types of robotics technology appear in different kinds of devicses. They’re not all humanoid but they can be adding all kinds of intelligent behaviors in mechanisms. 

Interviewer: 

Just to kinda put some dates on that, what year did you go to UNC and Ford and Stanford and NSF? 

Jing Xiao: 

Oh, yeah, I went to UNC Charlotte in 1990 and went to Ford after I got tenured in 1997, and Stanford 1998, and then NSF also starting from 1998. And I was there serving the program for two and a half years. 

### Work at Ford, Stanford University and National Science Foundation

Interviewer: 

What kind of work did you do at Ford while you were there? 

Jing Xiao: 

Optimization of assembly sequencing. They have the assembly line, and a vehicle starting from just the shell of the body and going through the assembly line and get everything painted, doors and so on. And then there’s a lot of issue of how you going to sequence this, which things to put first. And also, because the assembly line has a mixture of different vehicles, if-- how do you actually put vehicles of different types in a sequence that’s most efficient for the assembly operation. 

Interviewer: 

Interesting. Who are some of the people you worked with when you were at Stanford? 

Jing Xiao: 

Well, I will say my host was Jean Claude Latombe, famous roboticist and his book “Robot Motion Planning” has been very widely used. But I also interacted with a professor Oussama Khatib. 

### Human Augmentation Elements in Medical Robotics

Interviewer: 

Okay, and for the NSF program, had you done much work with human augmentation elements before or was that sorta new? 

Jing Xiao: 

No, the human augmentation is an element of the program. So the idea is robot is not just a monolithic entity by itself. It can be part of-- in one form, it can be part of a accessory on the person to extend a person’s capability. So that’s one idea and also another meaning of human augmentation is that robotics can assist people to perform better rather than replacing people. That’s... Interviewer: 

Great, and do you remember any of the projects that were funded while you were there or things that you learned 

<inaudible>? 

Jing Xiao: 

Yeah, certainly a lot of projects were funded. That’s a very long, long time... 

Interviewer: 

Any examples? 

Jing Xiao: 

...ago. 

Interviewer: 

Even in general, what kind of work were people doing? What were the kind of... 

Interviewer: 

It’s all kinds of work. 

Interviewer: 

...major things that people were focusing on at the time. 

Jing Xiao: 

At the time, one big thing is medical robotics. Johns Hopkins formed a engineering research center that was really around that time. For a professor Russell Taylor, he led the effort. So one idea that was very impressive was the steady hand robot. So the human surgeon holds the robot and the robot will make-- the control of the robot will make any operation more precise and less tremor, more steady and so on. So that’s a very good example of human augmentation. 

### Developing Real Time Motion Planning Algorithms

Interviewer: 

Great, great, and then what kinda projects did you work on when you came back to UNC after the NSF? 

Jing Xiao: 

I have-- well, the-- that’s a-- let me think a little bit about that. Oh, yeah, during my positon, during my service at NSF, I still had students working in research labs. I continued supervise my student when student work on this robot motion planning in the contact space graduated soon after I came back. And then I also worked on-- I was always interested in real-time motion planning algorithms and anything to do with some uncertainty. It started with considering uncertainty in assembly. Then I was intrigued by how to make robot moving around in a environment with unknown object motion. Because, if a environment is completely known, we can always do off-line planning to get the path or trajectory for robot to move around. But if the environment is dynamic and you don’t know how the other objects or people or obstacles move, then your planning algorithm has to be in real-time. So how can we deal with that? So I had a new student and we worked on the plan and called it real-time adapting motion planning. And especially focused on high degrees of freedom robots like mobile manipulators, not just mobile robot. A lot of people working on mobile robot but we were interested in manipulation and in high degrees of freedom robots moving around doing different manipulation tasks and how a robot can function in this environment without knowing others’ movements. 

### Work in Haptics

Interviewer: 

Interesting. So you mentioned some of your students but maybe you could tell us some of the names of students and PhDs that you’ve supervised who have gone on to work in academia or industry and still work in robotics. 

Jing Xiao: 

Well, I don’t-- actually, I don’t think they work in robotics. So, yeah. I don’t have a-- so far-- I have very good students but they move on to different things after the graduation. I had a good student on haptic-- oh, another thing is haptics. I started to be more and more interested in haptics interaction. So I had students working in haptics rendering and especially the problem of multiple contact situation. When you have a tool held by a person to make all kinds of different contacts with an environment. How can you most accurately simulate the force response and also the graphics display? Yeah, and the deformable object, some object with deformations so it certainly worked in those areas too. And, more recently, I got intrigued by the so-called continuum manipulators. And these were first-- were inspired by structures found in nature, in invertebrate structures such as a octopus tentacle or a elephant trunk. So I collaborated with Clemson University, a professor in Walker’s group, in putting autonomy into these kind of robots. They developed the robot, the hardware, and they have a way of-- a remote control teleoperated robot. But there was no autonomous algorithms at the time so our group contributed in designing and implementing the algorithms. So autonomous grasping objects in cluttering environments, avoiding other obstacles with this type of elephant trunk robot. 

### Challenges of Continuous Manipulator: Deformity and Degrees of Freedom

Interviewer: 

What are the big challenges of this kind of continuous manipulator? 

Jing Xiao: 

Continuous manipulator is very high-dimensional and that’s certainly a big challenge. And also the form, because the-- well, it form the forms. How to say it? It deforms, unlike articulate arm. Our arm have finite number of joints or, if not our arm, the robot arm. And each link is pretty ridged. It doesn’t deform. But continuum manipulator deforms everywhere and then, when we plan its motion, you have to consider all these high degrees of freedom. 

Interviewer: 

Are they related in any way to the snake type robot? 

Jing Xiao: 

The snake robot-- yeah, at the high level it seems much like a snake robot looks like that, that kind of elephant trunk too. But fundamentally snake robots are different because they’re so-called hyper redundant robots with a lot of joints. But, between two joints, there’s a rigid link. It’s just very short rigid link. A lot of rigid links together so that they have hyper redundant. Hyper redundant means a lot of degrees of freedom to make a snake robot behave more like a continuum robot. So it’s like an approximation of a real continuum robot. 

Interviewer: 

They also use a lot of coupled oscillators for motion and things like that. 

Jing Xiao: 

Right, exactly, because of that. So the way of actuating the robots are different. 

### Designing Elephant Trunk Robot

Interviewer: 

How is your snake robot designed? 

Jing Xiao: 

I didn’t de-- no, but the elephant trunk. 

Interviewer: 

I know but-- the elephant trunk, yeah, <inaudible>. 

Jing Xiao: 

Yeah, yeah. I didn’t design them. The professor in Walker’s group at Clemson designed those. They’re pneumatic. They have kind of tubes and-- several tubes together to form a section and the section can contract or extend its length and change curvature and so on. And multiple sections connecting tangentially to form that. So the control is section by section in a way. 

Interviewer: 

So you can get arbitrary motions with your autonomous system of the <inaudible>? 

Jing Xiao: 

Well, it has finite number of controllable degrees of freedom. So I cannot say the motion’s arbitrary but it can cover a lot of shapes. The combination is pretty big. 

### Collaborations

Interviewer: 

Were there any other groups or universities or groups that you collaborated with over the years? 

Jing Xiao: 

Yeah, I did a-- yeah, I forgot to mention. Yeah, it’s just a lot of things when you do think about. I forgot to mention a very great collaboration with Catholic University of Leuven in Belgium. We collaborated on autonomous complying motion from planning to execution with force sensor attached to the robot. Going through-- so it’s general methodology, going through different kind of contact situations. It’s not limited to a particular type of object or assembly. So that work applies to arbitrary polygonal shaped objects. 

Interviewer: 

Who were the P.I.s? 

Jing Xiao: 

In Belgium? Professor Joris De Schutter and Professor Herman Bruyninckx. Yeah. 

Interviewer: 

Good. Were there other collaborations as well there? 

Jing Xiao: 

My collaboration with the KU Leuven, that group, and also with the Clemson group are the most significant ones. But I also collaborated with General Motors more recently on, again, assembly. Because this is still not the solved problem, more focused on so-called surface assembly to try to align two parts by overcoming uncertainty. 

### Challenges to Developing the Robotics Field

Interviewer: 

What do you see as the big research questions and challenges for robotics going forward? 

Jing Xiao: 

I think going forward, one of the biggest challenges is also what I have an interest in, is manipulation. We see autonomous cars, some other great advance. But we haven’t seen really versatile manipulators that can operate in some generic environment without a lot of engineering of the environment to accommodate the robot. 

Interviewer: 

So it’s the dynamic and the clutter and things like that... 

Jing Xiao: 

Yeah. 

Interviewer: 

...that make it a little difficult. 

Jing Xiao: 

Yeah, and sensing and perception and integration of perception and action. Still. Yeah. And not at the non-contact level but at the contact level. It’s a contact sport. 

Interviewer: 

Do you see this playing out generally? I know you’ve worked mostly in a lot of these situations where you were doing assembly but do you-- when you’re thinking of this, often people talk about robots in more natural environments or other human environments. Is that an area that you see... 

Jing Xiao: 

Yeah, definitely. That’s why I uncertainty handling. I mentioned my work with a student real-time adaptive motion planning. That’s for moving in the environment with other moving things, maybe human, maybe some vehicles or something else. And how to make sure the robot can navigate safely. But that’s definitely still a challenging thing, although a lot of progress has been made and we will see more people-- actually, it’s always the case there are researchers on mobile robots than on manipulators. 

### Sources for Grants and Research

Interviewer: 

Where have been the sources for your grants and research <inaudible>? 

Jing Xiao: 

Mostly NSF and some industrial funding too. 

Interviewer: 

The automotive primarily? 

Jing Xiao: 

Automotive and also more recently in nuclear power industry because the site director of something called Industry University Collaborative Research Center funded by NSF in our university. 

### Women in Robotics

Interviewer: 

Great. So I wonder if you would talk a little bit about your experience as a woman in robotics and what we might be able to do to increase the number of women in robotics. 

Jing Xiao: 

Yeah, this is-- I mean, the first question-- my experience as a woman in robotics, as I said, I never really consciously-- I wasn’t really conscious that I was a female, even though it was interesting when I first entered the PhD program at Michigan. It was interdisciplinary one and supposed to be very hard and there was an orientation for new students and faculty member were there. And, in the room, I was the only female student and there’s one female professor, Professor Janice Jenkins. And so the first sentence she said to me was, “You’re the only female student. I’m the only female professor.” So it kinda made me aware, “Oh, yeah. Indeed that’s the case.” There were very few females at the time but I guess that I’m not really very conscious about that because I don’t feel like because I’m a female I must be lacking something. I don’t really feel that way. 

Interviewer: 

So the P.C. meeting here is an all-female P.C. What do you think the... 

Jing Xiao: 

Impact? 

Interviewer: 

Not the reason-- or impact or <inaudible>... 

Jing Xiao: 

I think the impact will be great. It makes women in robotics more visible and can be more inspiring to female students, because they can see all these role models. So I really think the impact will be very significant. 

### Robotics in China

Interviewer: 

I have a-- unrelated to that question but I’m curious. Do you have knowledge of what’s going on in robotics in China? Have you ever worked with people or <inaudible>? 

Jing Xiao: 

Yeah, I collaborate, certainly collaborated with people in China, especially with Beihang University in haptics. My impression is robotics in China is still mostly-- well, maybe I don’t really know too much so I probably shouldn’t say because I should say I really don’t know too much what’s going on. And I think there’re more robots. They build robots and for different purposes for search and rescue or for industrial applications. But, on the other hand, from the perspective of algorithms and programs, I don’t see too many-- at least too many innovation. Or maybe it’s just that I don’t know too much. 

Interviewer: 

Yeah, we haven't had the opportunity to talk to too many people from China so that’s why I’m asking. 

Jing Xiao: 

Yeah, I think it’s probably better to just cut off what I said... 

Interviewer: 

Oh, sure, no problem. 

Jing Xiao: 

...because I don’t really know. 

Interviewer: 

You mentioned that you collaborated with some people from China. What kinds of things have you collaborated on? 

Jing Xiao: 

Haptics. 

Interviewer: 

Mm-hm.. and why was it particularly interesting to collaborate with <inaudible>? 

Jing Xiao: 

I think it was more like just the problems because they came to me and said, “Oh, you did this work and we have this similar concern. We want to focus on a rendering of a force response for very complex interaction situation with contacts. So it’s really just research topic oriented. And the same thing with my other collaborations. It’s not because of other reasons. The reason is just pure common interest on particular research problem. 

### Robotics Program at University of North Carolina at Charlotte

Interviewer: 

I wonder if you could talk a little bit about what was going on in robotics since you first hit North Carolina and Charlotte, when you first got there and how that program has grown and evolved <inaudible>. 

Jing Xiao: 

Oh, well, there was no robotics then and we had some people in different departments that teach robotics. And I think one 
faculty member taught robotics then and he left, maybe for various reasons. Then, I was mostly by myself and my students doing robotics work for many years. And, more recently, I have a colleague who’s also in robotics and we are seeing more and more interest from students to learn about robotics and to do research in robotics. 

Interviewer: 

Is there artificial intelligence courses or is it mostly control-oriented? What’s the academic environment around robotics? 

Jing Xiao: 

I think more lean towards algorithms and certainly the basics. You have to learn the basics in order to do manipulation. If you don’t understand kinematics and dynamics for an arm, you cannot really do too much. 

Interviewer: 

Do they have the engineering students as well as computer science students <inaudible>? 

Jing Xiao: 

Yeah, we have a engineering-- so we’re in a different college now. We used to be part of engineering but now we have our own college, College of Computing and Informatics. The College of Engineering also has the faculty members interested in robotics. More interested in the education part of robotics and they run robotics summer camps, for example, very successfully. The robotics summer camps are the most popular ones. It’s very difficult to get in. One easily get on the waiting list. So they’re more interested in that. 

### Advice for Prospective Students

Interviewer: 

Great, and the question we always ask is what sort of advice do you have for young people who are interested in a career in robotics? 

Jing Xiao: 

I think I-- well, certainly-- first, one needs to be motivated. You want to solve some problems with robotics. Then, with that goal in mind, next one needs to really build the foundation to learn all need to be learned. And then, just let your natural creativity and imagination take you. 

Interviewer: 

Great. Is there anything that we didn’t cover that you wanted to talk about or any particular projects <inaudible> that you remembered that we didn’t talk about? 

Jing Xiao: 

Not really. Actually, I don’t know. 

<crew talk> 

### Involvement with the IEEE and the Robotics Automation Society

Interviewer: 

You could also talk a little bit about your involvement with the IEEE and the Robotics Automation Society and some of the service roles that you’ve held. 

Jing Xiao: 

Yes. Yeah, I got involved with those pretty early. I was elected as an administrative committee member back in 1999. So I served for three years starting from 1999. That was my first kind of interaction with the IEEE Robotics Automation Society. And then, over the years, I always got involved to some degree. I was in the members and-- what do you call? Membership Activities Board. And I remember we first talked about how to lower the barrier for students and to the society, and to lower the member ship fees for students, and to try to attract more students. And also the next thing is try to make sure the students find the society useful and beneficial for their careers and they want to stay on after their graduation. Currently, I’m serving as the vice president for Member Activities, board. Our major goal is to try to retain our younger members, especially two to five years’ membership, and still continue attract student members. 

Interviewer: 

What are some of the ways that you’re trying to do that? 

Jing Xiao: 

I don’t know if everything so be in this but... 

Interviewer: 

No problem. 

<off topic conversation> 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Jing_Xiao&oldid=195247 "
