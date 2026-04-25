1 About Rolf Pfeifer 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Introduction 4.2 Carnegie Mellon 4.3 Interest in AI 4.4 First Robotics Project 4.5 Other Bio-Robotics Projects 4.6 Evolution and Challenges of Bio-Robotics 4.7 Soft Robotics 4.8 Robotic Vision 4.9 Swizz Robotics Community 4.10 Ph.D. Students 4.11 Future of Soft Robotics and Bio-Robotics 4.12 Advice for Young People 

## About Rolf Pfeifer

Rolf Pfeifer was born in Zurich, Switzerland. He received his master's degree in Physics and Mathematics, and his Ph.D in Computer Science from the Swiss Federal Institute of Technology (ETH) in Zurich. He then spent three years at Carnegie Mellon and Yale as a post-doctoral fellow working on computational models of emotion, artificial intelligence, and language. In 1987, he joined the Computer Science faculty at the Department of Informatics, University of Zurich, as well as became director of the Artificial Intelligence Laboratory. Pfeifer also worked as a visiting professor and research fellow at the Free University of Brussels, the MIT AI Lab, the Neurosciences Institute (NSI), the Beijing Open Laboratory for Cognitive Science, and the Sony Computer Science Lab in Paris. Retiring in 2014, he continues to serve as a professor at Osaka University and as a visiting professor at Shanghai Jiao Tong University. He was also elected Deputy Director of the National Competence Center for Research in Robotics (NCCR) in Switzerland, and as a member of the FET flagship pilot integration team. 

Pfeifer's research interests include bio-robotics, soft robotics, artificial intelligence and evolution, autonomous agents, modular robotics, self-assembly, and educational technology. His work include involvement in several robotics projects, over 200 scientific publications, and four published books. 

In this interview, Rolf Pfeifer discusses his work in robotics, focusing on artificial intelligence and locomotion. Describing the influence of human psychology and intelligence on his research, he outlines his early work with cognitive robots and AI and his later work in bio-robotics. He discusses the challenges and breakthroughs of his work and of bio-robotics as a whole, as well as the evolution of robotics throughout his career and its future applications and goals. 

## About the Interview

ROLF PFEIFER: An Interview Conducted by Peter Asaro with Rolf Pfeifer, IEEE History Center, 15 July 2011. 

Interview #744 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Robert Riener, an oral history conducted in 2011 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Rolf Pfeifer 
INTERVIEWER: Peter Asaro with Rolf Pfeifer 
DATE: 15 July 2011 
PLACE: Zurich, Switzerland 

### Early Life and Introduction

Peter Asaro: 

So if you could start by introducing yourself, telling us where you were born and where you grew up and went to school. 

Rolf Pfeifer: 

Okay. I was born actually in Zurich in Switzerland and then I went to ETH studying physics and mathematics. And then I started working at a psychology department doing simulation of dreams which was a project at the time that was funded by the Swiss National Science Foundation and we working together with a clinical psychologist with psychoanalysts trying to develop a computational theory of conflict which is underlying and it’s a real Freudian sort of thing. And now, I think, with the hindsight I have to admit that not too much came out of that project really. But it sort of got me into this – we were working with people in Sweden who were in computational linguistics. And so they were using methods from artificial intelligence at the time and so we were applying these methods then also using at the time fashionable programming language LISP that people were using at the time. That sort of got me into artificial intelligence. 

I also then did a Ph.D. also in Zurich at ETH which was interdisciplinary between computer science and psychology on simulation of cognitive processes. Then I did a post doc in the U.S. actually with Herbert Simon who is one of the pioneers of artificial intelligence, very early pioneers. And he’s also a Nobel Prize in economics. And so I did this post doc and I was working on computational models of emotion. And then after about two years CMU I went to Yale working with Robert Abelson and Roger Schank was also at the same institute and at that time Schank and Abelson were sort of the big figures in artificial intelligence and language. And then I think I wasn’t very happy with these computational models. I sort of had the feeling that something was missing and that we didn’t learn very much about emotions by developing this computational models. And then someone from Zurich said, hey, we have a position, why don’t you come to Zurich and do a class on expert systems and at the time I didn’t know what expert systems were but then I got into it and I thought this is not uninteresting. 

And then I started teaching expert systems. And then they actually had an opening for a professorship at the University of Zurich and I applied for it and luckily I got the position which was, I think, about almost 25 years ago. And then I built my research group and we were doing actually expert systems. We were developing, we worked with companies like, of course, in Switzerland you work with banks, right. I worked with banks trying to do commercial loan assessment, develop systems with these rules if these conditions, then this, if this then this. So you have hundreds of these rules and then you try to get a decision. Basically autonomous problem solving systems, that’s what we were developing. And with companies we also did technical diagnosis of laboratory automation systems, laboratory robots and things. And we really had many projects also with insurance companies, also with Schindler, the company producing elevators, for configuring elevators it’s very complicated sort of thing. And we built some beautiful prototypes and demonstrated these prototypes to the people, to the management and everybody was excited about them. And in one case, I think, I the case of Schindler actually they took it into daily practice and after half a year without any reason basically they took it – they didn’t use it any longer and this is basically what happened with all of the systems that we developed. There were either not used or they were taken out of use after a relatively short period of time and then they ended up in the training departments or educational departments. And without that, that was kind of okay but something essentially seemed to be missing. And then we started looking into that and I actually had two Ph.D. students just looking into what’s wrong with what we’re doing here. And we had the impression something was fundamentally wrong and that was a time when I think Winograd or a draft of Winograd’s book was circulated before it was published. It was called “Understanding Computers and Cognition”, I think, that was the one. We looked at that and also I knew we had very good context with William J. Clancey. He was at Stanford at the time. He’s now, I think, at NASA Ames. And he was working on the Mycin expert system which was for diagnosis of, I think, blood diseases, something like that. He had been working on the Mycin system so he was a real expert on expert systems. Every couple of years he wrote a provocative paper that sort of shook up the community and so we invited him to come here for a week or two weeks and give seminars and trying to sort of figure out what’s fundamentally wrong with what’s going on and looking to Winograd. Also rereading Dreyfus, what computers can’t do or what computers still can’t do. And then, I think, we began to understand that one of the – it’s a completely like having a set of logical rules to model the human intelligence is just totally completely utterly inappropriate. It will never work. And then also what’s completely neglected was perception, the interaction with the environment. All of these systems all started – I mean if you – yes, and one of the things we did we coupled up with psychologists trying to understand human expertise. And so we did a lot of studies also with these companies, with these experts, following the experts to the companies when they were doing their job. And it turned out to be very, very interesting. And it’s basically I mean if you look at a medical doctor – I mean the medical doctor, let’s say a family physician sort of – I mean he or she looks at someone and says, well, how many do you smoke, right? It’s basically a lot is in this perceptual process. And a lot of the sort of reasoning is happening before you even start thinking about logical roles. We also looked at to study experts at banks, doing commercial loan assessment. And they sort of flick through the things very quickly and then they start asking questions. And also one of the things that we saw is they don’t sit there and then do the commercial loan assessment. But throughout the year the customer says well I need the financial transfer, this and this and they say well, how is it going. And so basically he constantly is building an image of the company and of the management. And then the commercial loan assessment is not like a task. But we were thinking in terms of having a task, a system that you start up and solve today. 

So there were many, many issues and then we thought, okay, this is not going to go anywhere. And then also some of the companies, I mean, there’s real hype in the eighties with expert systems. So we realized it’s not going to go anywhere and some of the companies started going bankrupt. And then I had a sabbatical and I went to Brussels in Luc Steels ’ laboratory and he had a very interesting – he was sort of apparently encountering similar problems and he had an interesting setup there and he had visitors from MIT coming over. I think Maja Matarić was there. Rodney Brooks was there. And then Tim Smithers from Edinburgh was there. And he organized a workshop in Corsendonk which is a former monastery. And he had invited a lot of people. William J. Clancey was there. Stevan Harnad was there. 

### Carnegie Mellon

Peter Asaro: 

Let’s go back a little bit and then we can come back to your work with Steels. About what year was it that you went to Carnegie Mellon? 

Rolf Pfeifer: 

I think it was ’82 to ’84 or something like that roughly. 

Peter Asaro: 

You were in the AI Lab working with Herb Simon. Were you interacting at all at that time with the robotics lab? 

Rolf Pfeifer: 

Not very closely. They had some demonstrations. Marc Raibert was there at the time and he was working on his pogo stick robot. And I have to say I was fascinated by that and I was also fascinated by the fact I mean I come from Switzerland, the Swiss are kind of sober, down to earth people, serious. And then you go there and then you see one of the most advanced research labs, you see kind of a pogo stick hopping around. And so I asked myself who – basically actually I admired the situation that someone would be able to convince a funding agency to give them money to build a sort of hopping pogo stick thing. I was fascinated. I was also fascinated by the argument that he said, “Well, if I can solve the dynamic movement problem or locomotion problem with one leg I can also solve it with two legs.” We didn’t really interact. I was more interacting with Simon and Newell and also more with the language people. John Anderson was there at the time, the act… 

Peter Asaro: 

Spreading <inaudible>. 

Rolf Pfeifer: 

That’s exactly that sort of thing. So I was more interacting with that community, so the more let’s say core artificial intelligence community rather than the robotics community. That only started when I then went to Brussels actually. 

Peter Asaro: 

What was it like to work with Herbert Simon? 

Rolf Pfeifer: 

Well, of course, he wasn’t there very often. He was, at the time, I think building a cognitive science program for the Chinese government. And I really admired him because we must have been already 65 or something but for this purpose he learned Chinese so that he could better interact with the people there. And I only saw him for an hour every two weeks or something but it was extremely productive. And he was listening. I was kind of basically a nobody and he was Mister Super Big Guy and he took the time to talk and I really learned a lot by just these short discussions that we had. 

Peter Asaro: 

And Newell, you had some interaction with him? 

Rolf Pfeifer: 

Not so much. I was working more with Simon. I was working more with John Anderson and the psychologists. 

Peter Asaro: 

Were there other graduate students you interacted with? 

Rolf Pfeifer: 

Yes. With the graduate students, actually, most of my interactions were with the graduate students. David Nicholas who then started working for Martin Marietta which Americans apparently don’t care. If I did a military project here at the lab I think about 80 percent of my collaborators would immediately leave. Here in Europe – also the European Union does not fund military research. And Pat Langley he was a machine learning guy. He was a post doc at the time. I interacted and also learned a lot from him, so the whole machine learning stuff. 

Peter Asaro: 

Was it at that time there, this conflict between the logical approach to AI and the more statistical to approach is? 

Rolf Pfeifer: 

I think the more statistical approaches I think they were more appropriate but that wasn’t basically the dichotomy statistical or non-statistical or rule based because I always thought there has to be this random component but it was more like – and that only emerged later for me what was missing was basically the interaction with the environment and that can only be through a body. It’s the only means we can interact with the environment so we need to look at the body. And then when I was in – but you wanted to ask some questions. 

### Interest in AI

Peter Asaro: 

Well, maybe it’s a slight lead up to that. What motivated you for moving into physics and into the psychology lab that sort of started you down the AI? 

Rolf Pfeifer: 

I’m not a very goal directed person. I don’t have a goal and then I pursue the goal. I’m more like just sort of looking around and saying, oh, maybe that’s interesting. I think it was a series of coincidences. At the time – that was before I – after I finished my physics degree, I worked at ETH and we actually started a seminar on cybernetics and you were saying that you were into the history of cybernetics. We invited people from various disciplines to give talks who – for example, we had Gordon Pask. We had, oh man, it’s a long time ago. But we had some really interesting people. And then we had people from specific disciplines psychology or biology who were using principles that relate to – Thomas Charles Helvey was the guy from NASA. He was working on the pragmatoscope, which is maybe also of historical, I don’t know if you’re familiar with the pragmatoscope. 

Peter Asaro: 

I’ve heard of it. 

Rolf Pfeifer: 

Yeah, so he was there. And one of the people that we invited was Ulrich Moser. He was a professor of clinical psychology at the University of Zurich and he was also a psychoanalyst working as a practicing psychoanalyst. And he had developed together with one of this assistants a computer simulation model of neurotic defense processes. And he gave this talk and I have to admit I didn’t understand a word. And then there was his assistant talking about the notion of time in the simulation model which was completely – I had absolutely no clue. And then we had coffee afterwards and Moser said, well, he had this project on simulation of dreams with the National Science Foundation and he’s looking for someone who can do simulations. And then I said well I can do simulations but I’ve done simulations in neutron physics, neutron transport phenomena, which was, by the way a Monte Carlo thing. And then I said I don’t know anything about psychology at the time. I really didn’t know what neurotic defense processes are. I had absolutely no clue. And he said, “It doesn’t matter. I need someone who can do simulations.” And then he had a friend who was working in Sweden and that fellow was working with or had good contacts with Eric Sandoval,who was one of the first doing like computational linguistics in a serious way. And then from there we sort of got into this artificial intelligence like computation. 

Peter Asaro: 

To get back to that Corsendonk workshop conference, was it at that point that you sort of had the epiphany, the embodiment was the sort of missing element from these emotional models? 

Rolf Pfeifer: 

Well, it was a bit of a gradual process leading up to that. But then there that was kind of a big thing. And also David McFarland was there. Francisco Varela was there. And William J. Clancey and Stevan Harnad. A lot of people – I’m not sure maybe even Rodney Brooks was there. I think he might have been there. I’m not sure but he was visiting Brussels a couple of times Luc Steels’ lab and so I started talking to him. And then… 

Peter Asaro: 

What year was that right there? 

Rolf Pfeifer: 

The Corsendonk workshop, that must have been 1991, I think. And then, of course, I came across – that was also my contact with biology. McFarland was spending quite a bit of time in Brussels. He was from Oxford, one of the sort of really the top ethologists. And then I realized how hard it is to talk someone from another discipline. I mean it took me at least a year or two years before I even remotely understood what he was saying. That was the contact with biology. I started realizing that working with biologists can be very productive. It’s also very hard. And then I came across Rodney Brooks’ paper with the innocuous title “Robust Layered Architecture for Mobile Robots”, which is basically the subsumption architecture. And it had a very innocuous title but it was kind of – and then I started – I’m not sure I understood but I remember when I started in Brussels – I was in Brussels for a year and at the Corsendonk workshop I realized that I don’t know anything. I didn’t even know what a robot was so I had no clue about robots and that was a bit embarrassing. But Tim Smithers was there also and John Hallam. And from then John Hallam had done a lot of work on vision. I learned about vision, depth through motion and optic flow and all of these things which are very useful concepts. And from Tim Smithers I learned how to build Lego robots and fast robots. And then we actually started – we decided to do a European project called “Design Principles for Autonomous Agents” or something like that and that’s when we really got into robotics. 

### First Robotics Project

Peter Asaro: 

That was your first robotics project? 

Rolf Pfeifer: 

That was the first robotics project. 

Peter Asaro: 

And that would have been in the early nineties? 

Rolf Pfeifer: 

That was in the early nineties, yeah. 

Peter Asaro: 

And what was the goal of that project? 

Rolf Pfeifer: 

Well, the goal was sort of contained in the title are there or can we really figure out design principles for autonomous systems working. I think McFarland was part of the project. Luc Steels was part of the project. Tim Smithers and our laboratory. And I had a psychologist working on the project as well. And so to see whether we can sort of extract principles that characterize the behavior of sort of biologically motivated or oriented systems. I think that’s also when we got really into sort of biologically inspired robots. And McFarland had some very good, I think, very, very good ideas on how one could do that. He even called it – I forget. But I think that was when we started the bio-robotics thing and sort of trying to work out principles and just to jump ahead then when we – that was, I think, in ’99 when we published this book “Understanding Intelligence”, which then was basically a summary of these design principles. Summarizing basically ten years of research trying to figure out what these principles. 

Peter Asaro: 

And did you start by when you say a biological robot, were you looking at the sort of biological motivations and emotional drives? Or were you actually trying to take biological models, specific formal models and instantiate them in robots. 

Rolf Pfeifer: 

Well, one of the projects that we did is together with Rüdiger Wehner who is probably the world’s sort of leading or was the world’s leading expert on insect navigation. He had been studying this desert ant cataglyphis in Southern Tunisia that lives in a salt pan in Southern Tunisia. And he basically had been studying that for 25 years and knew a lot about these animals. And then the way it started – it’s typical the way things happen in our laboratory. One of my Ph.D. students who was a mathematician he had been interested in this bio-robotics thing. And then he met some Ph.D. students of Wehner’s, the ant navigation guy, and together with them, they started building robots that mimic some of the navigation behaviors of these desert ants. And then I realized that after a while that he had been doing that, hey, this is great stuff. And then we went to Wehner. Wehner didn’t about this. I hadn’t known about this at the beginning. And then we were both excited about this and said let’s do this. This is great stuff. And then this is – I think Dimitri Lambrinos is his name. He was really a pioneer of bio-robotics I would say. And then this turned into a big project. And so we also then took our robots – you know the desert ant cataglyphis has a really very sophisticated navigation system. They can go out – they basically live in the desert. Their nest is basically a hole in the ground. They come out of this hole. And then they go out in a sort of zigzag course and they come out when it’s hottest at noon. And they go out in this zigzag course up to, I think, 200 meters away from the nest. And then they go back to the nest in a straight line. And the question is how do they do this? And I think this is known. It has been verified in hundreds of experiments. And we reproduced that navigation behavior and then we could also make suggestions to the biologists on what they might actually look at because we couldn’t get the robots to do the right thing unless we introduce some assumptions and then we could ask them well can you look for these assumptions in real animals. That’s when really also the fascination with the bio-robotics really started. 

### Other Bio-Robotics Projects

Peter Asaro: 

What other bio-robotics projects did you pursue after that? 

Rolf Pfeifer: 

Many. I will not end anymore… 

Peter Asaro: 

The highlights. 

Rolf Pfeifer: 

Some of the highlights. I mean one of the highlights was there was a European project Virgo, vision based robot navigation. And it was mostly classical robotics people and very classical vision people I mean very good people but traditional. And initially they always called us the outliers because we were doing this kind of bio stuff. But then after about two years’ time everybody realized that this was really interesting and then we were basically sort of the highlights of the project. And I think people started realizing that this kind of research can be interesting. I think that was a really fascinating project. Another is concerning this robot here. That’s also bio inspired. It’s really not only trying to mimic sort of make the surface human like but also the bones, the tendons, the muscles. Actually, all of our projects, all of the projects that we do are bio inspired. We did some projects on underwater locomotion, basically robot fish looking specifically at materials, changing materials properties but maybe I’m jumping ahead here. The looking at dynamic movement of quadrupedal walking, bipedal walking. This is all bio inspired. Now, we have one project also on bivalves you know how they dig in the sand looking because morphology and surface characteristics there play an essential role. And then we have hand prosthetics projects which are, of course, also bio inspired. Then we had a project on programmable artificial cell evolution, also big European project which was then basically self-assembly. It was in self-assembly vesicles, also inspired by biological cells. I think all of the projects that we do are one way or other biologically inspired. 

### Evolution and Challenges of Bio-Robotics

Peter Asaro: 

And in sort of bio-robotics more generally, what would you say have been the biggest challenges and the biggest kinds of breakthroughs over the past 20 years of bio-robotics? 

Rolf Pfeifer: 

Okay, that’s a difficult question. I think a lot of work has been done – if you really look at bio-robotics I mean there is also, of course, like a neural computation, computational neuroscience which is more about the neural system. That’s, of course, also bio inspired or at least some people are very bio inspired. But bio robotics I think a lot of work initially I think a lot of work was done on movement and locomotion. 

<knocking interruption> 

<break in recording> 

Rolf Pfeifer: 

Okay. We get back to the big challenges or the big highlights in bio inspired robotics. I think the work – I think some of the seminal work in the fields really has been done by Barbara Webb with the cricket phonotaxis. And she also looked at the neural systems and was developing models of spiking neurons and she was really having the real crickets interact with the robotic crickets. I think that’s definitely one of the highlights I would say. I would also say that our kind of desert ant cataglyphis robot is kind of a highlight because we also took the robot to the desert so that it had to function in exactly the same environment that the ants had to function. And I think we could reproduce these behaviors, the behaviors of the ants to a good extent. Also I think I shouldn’t forget the work by Srinivasan which I think is simply brilliant. And he does the experiments on the animals, on the bees and then he builds the robots that exploit these principles like optic flow, optic flow based navigation and kind of visual odometry by integrating optic flow and things like that. So I think that’s absolutely brilliant work. Now, I’m sure I forget really significant work that people do. And now it’s a big community. Where are the biggest challenges? I mean there are so many challenges but maybe I can come to that when we talk about soft robotics. 

Peter Asaro: 

Maybe just more generally, has it been a challenge to promote bio-robotics within the robotics community? 

Rolf Pfeifer: 

Absolutely. Personally, I don’t come from robotics. I come from physics, mathematics, computer science, psychology but not robotics, not engineering. I’m basically not an engineer. Sometimes I say well I used to be a scientist and now I degenerated into an engineer. I basically learned on the job by actually trying to build robots. I learned about engineering. Now, of course, on the one hand I think that’s a disadvantage because there’s so much knowledge around in engineering that makes your life easy when you’re building these machines. On the other hand, it was maybe a good thing because then we didn’t go along with the mainstream. And so we could look at the field sort of from the outside. Now, I guess one of the problems that we had and still have is what some people call proof by video. Basically, we build a robot and then it does something interesting. Of course, we always take videos and then we go to a conference and say see, it works. And then the people from real robotics they come and say well, but you didn’t prove anything. What are the limitations? I think one of the problems – we were facing a number of problems in getting people interested in bio-robotics. One was, I think, our own scientific methodology which was not so scientific. I mean I had two ethologists working in my laboratory who had done a lot of experiments with animals. So they knew how to do experiments. And so they were trying to do some experiments with robots, systematic experiments with robots. Now, there is a good reason why this is not often done because we build a robot, we make some experiments and then we immediately see where it doesn’t work, that we have to improve the robots or we’re not going to run N equals 100 experiments with a robot if we know already that we want to improve the robots. So I think there are good reasons why this is the case. And the other thing is that the people from let’s say control theory more let’s say traditional manufacturing robotics they either thought this was not relevant, not interesting, or they thought it’s sort of not really scientific, right. But now and I think it just took a while and then we started publishing and we started writing books and going to conferences. Initially – that’s maybe a point, initially – well, we didn’t go to the artificial intelligence conferences anymore because we didn’t believe in the computational model of intelligence anymore. We avoided these conferences because initially we wanted to convince these people but people who don’t want to be convinced you know it’s very difficult. And so we went to other conferences like adaptive behavior or artificial life, also maybe some neural networks conferences they had an interest. But we didn’t initially go very much to the robotics conferences. Only over time I think there were, I think, at the robotics conferences people were organizing tracks on biologically inspired robotics. Now, at the recent ICRA conference in Shanghai that was full of bio inspiration. So I think the bio inspiration is now really getting into mainstream robotics. Also surprise, surprise I was in invited to give the opening keynote lecture at the IROS conference in November 2010 in Taipei and IROS is really also one of the big traditional robotics conferences. That was a big surprise. It seems that this kind of thinking is getting into mainstream robotics. Yesterday, we had Paolo Fiorini an Italian control engineer and he was here, he said, “Well, my kind of robotics is very boring. And your stuff is so much more fun I want to learn about this and make my courses more exciting.” I think it’s really beginning to change. But still I think one of the challenges will be to put this on a better more formal basis. I think that’s at the moment still lacking to a large extent. 

### Soft Robotics

Peter Asaro: 

How were you led into the idea of soft robotics? 

Rolf Pfeifer: 

Okay. I forget which conferences that was but that must have been something like twelve years ago or something. I was giving a talk at a conference, I forget which conference it was and I was talking about the importance of materials for intelligent behavior. And then I think most people there thought now, he has completely gone off the deep end but we were pursuing this idea. For example, dynamic movement we were working on quadrupeds and having springs on having some passive joints and having springs on the passive joints gives you enormous leverage on stability and robustness over uneven terrain. And I think we even won one of the competitions, the robotics – I’m not sure it was a robotics conference, but a conference as sort of a race with this very simple robot just exploiting material characteristics. And since then we have been pursuing this idea of materials, also with underwater movement and locomotion. The material characteristics of the tailfin, for example, are extremely important. You know, low stiffness of the tailfin for long range cruising, low frequency, high stiffness and high frequency for fast sort of shooting away. And then we were looking at changeable material properties and then we realized well you grasp a glass with your hand. That’s very easy to do. You don’t even need to know the exact – that cup over there has a not very usual shape. You don’t need to know exactly about the shape. You just with a certain force go bend your fingers around the glass. And then on the fingertips and on the fingers you have the deformable tissue. So as you grasp the hard object, the tissue passively without control from the brain adapts to the shape of the glass. And then you really just start – if you think about having what is it called thimbles on all of the fingers trying to grasp a glass it’s next to impossible to do. So then you start realizing what the materials actually do for you. And then we looked at this skin about what is it I forget exactly several hundred touch and temperature sensors and pain sensors per square centimeter on the fingertips. They still work when the tissue is deformed. And you can read it out in parallel. It’s robust and when it breaks it actually regrows. So we realize that there is some enormous challenges. And if you look at the current state like a robot like that has maybe one or two or a couple of touch sensors on the fingertips but that’s it. And I think if we had skin, something like human-like with the human-like characteristics of skin that would be a quantum leap in robotics. I think materials. I think in the future there is this flagship project of the European Union that we’re working on, the robot companion project which is a very, very large project just like putting some person on the moon. And the idea is to have a project 100 million euros per year for a period of 10 years and so we’re in the process of preparing that. That’s a new funding scheme of the European Union future and emergent technologies. And in there we are really focusing on materials. And I think probably half of the whole project is going to be materials. We now cooperate very closely with material scientists. And so I mean for me it’s a nice development because originally people felt this – I mean what is he talking about. And now it’s clear that materials is going to be a key technology for intelligence systems. 

Peter Asaro: 

Who are some of the other collaborators on the robot companion project? 

Rolf Pfeifer: 

Well, at the moment I think there are – in preparing the proposal about 200 people are involved. And the coordinator of the whole thing is Paolo Dario at the school of Scuola Superiore Sant’Anna in Pisa. And then other people who are involved is Roberto Cingolani who is the director of the Italian Institute of Technology in Genoa and he’s a materials scientist. And then, of course, like everybody in Europe is involved Tamim Asfour, Rüdiger Dillmann, Martin Buss, Gordon Cheng. I mean you name them. I mean just anybody will be who is in – let’s see there are two things. One is the human brain project by Henry Markram, simulation of the human brain. And the other one is this robot companion project. And whoever is not involved in the human brain project is in the robot companion project. 

Peter Asaro: 

Who’s going to marry the two together? 

Rolf Pfeifer: 

Yeah. Some people have thought about that. Some people have thought about that, yes. So you were asking about soft robotics. And then we looked at that and then we realized if you look at the biological system I mean, of course, we have teeth and we have some bones which are a bit hard but not really hard and all of the rest is soft, the muscles, the tendons, the tissue, the facial tissue. Everything is soft. The organs are soft. Biological systems, biological intelligence systems are soft systems. If you want to go to the next step of robotics I think we need to look at soft systems. 

Peter Asaro: 

You mentioned some of the spring based systems. Can you talk a bit more about the importance of tendons for motion in robotics? 

Rolf Pfeifer: 

Yes. It depends on your goals. I think we always have to keep in mind it depends on the goals. If your goal is to manufacture cars, then it may at this point not be a very good idea to think about soft robotics because they have methods and tools that work just perfectly. Why would you want to change that? If your goal is to have a cute robot that can do nice things then maybe the ASIMO approach is a good approach or Sony QRIO or NAO or whatever. These robots all have the motors in the joints except maybe for the hands. I think for the hands they’re also tendon driven because you can’t have motors really in the hands. Now, if you have a tendon driven system then you don’t need to have the motors in the joints and you can have them in various places. You can have them distributed throughout the organism and then the tendons are pulled over the joint. If you are interested in biomimetics, in biological inspired robotics, of course, you have to have a tendon driven system. Now, the question is what are the advantages that this gives you? There are also disadvantages. I mean you have a kind of – it’s very nonlinear the whole thing, the muscles. You cannot stretch them. You can only pull them so you always need a flexor or extender. One advantage is that you have a compliant system and which is passively compliant so you don’t need to control for the compliance. And then if you have muscles, if you have artificial muscles rather than electrical motors you can dynamically change the stiffness. So basically what the brain does in walking, for example, in dynamic movement is not so much controlling in detail the trajectories of the joints, of the knee joints, or the elbow joints, but controlling the body posture which is sort of the global dynamics of the system. And then controlling the stiffness of the muscles, low stiffness, almost passive in the swing forward, high stiffness on impact. And then it’s as if – and then the brain doesn’t need to do much to cope with the impact. It’s basically outsourced to the morphological and material properties of the organism. And then the question is not so much control or not controlled but at what level do you actually want to apply the control. Now, muscle stiffness is a global parameter and then, again, so you have body posture, muscle stiffness and then you can leave everything up to the local dynamics. That then just basically takes off. Now, the fact that the knee joint or the elbow joint in walking is not directly controlled does not imply they’re not doing the right thing. They self-organize into the property trajectories. So I think we need to think more in terms of exploitation of passive dynamics, self-organization and emergence ultimately every behavior is an emergent behavior. And then if you have these tendon driven systems with artificial muscles it’s very easy to change from active mode to passive mode which is much, much more difficult to do with when you have electrical motors in the joints. 

Peter Asaro: 

And as far as bipedal versus quadrupedal it applies to both it applies to both sets of… 

Rolf Pfeifer: 

It applies absolutely to both. Yes, exploitation of passive dynamics I think is essential for both also for very complex organisms, not only for passive. Dynamic walkers which are these very simple walkers that can walk down the ramp without control. But it also applies to complex biological systems. They all exploit the passive dynamics. And I think it’s much easier to do with artificial muscles, tendon driven systems. 

### Robotic Vision

Peter Asaro: 

Okay. That was so fascinating I don’t know what to ask next. I’m still thinking about that. What about in terms of perception? How does soft robotics effect that? Are there ways of thinking about vision and other forms of perception? 

Rolf Pfeifer: 

Yes. I mean there is, of course, the algorithmic computer vision community, robotics vision community. If you look at biological inspiration then you realize and this is nothing new that I’m saying now you realize that movement is extremely important for vision. We are basically – it’s never static. And well there’s much to be said about that. We were looking, actually, at the time and when I was in Brussels working what John Hallam and Tim Smithers and Luc Steels we were looking at also ecological psychology. I think Michael T. Turvey he was somewhere in Connecticut. 

Peter Asaro: 

J.J. Gibson? 

Rolf Pfeifer: 

J.J. Gibson, yes, and Turvey is kind of a Gibson student. Now, I think Gibson was a bit too much sort of putting the affordances which is basically affordances, you know, the things that you can do with objects too much into the environment. I think affordances are really an interactive thing between an agent and the environment because the perceptual and motor abilities of the agent are, of course, crucial for the affordances. But we’re looking at Turvey and Turvey had all of these patterns with optic flow. And so we started really looking into optic flow. And because we were working on insect navigation or started sort of looking at the insect navigation I mean they do a lot through optic flow. I mean they do odometry, centering. There was just an article – also I think one of the highlights and that reminds me, one of the highlights in bio-robotics was Nicolas Franceschini in Marseille. He built the complete analog insect eye that was a robot that was on wheels but he was a neuro biologist looking at insect vision. And he had built this insect eye completely analog robot. And by the way, one of my – and we had good contacts. We learned a lot from Franceschini. And one of my post docs that I had Ralf Möller who is now at the University of Bielefeld he had built a robot without software that could learn, an analog. We just called it the analog robot. It was mimicking the landmark navigation behavior of the desert ant cataglyphis. It was a completely analog robot but still it could learn and that was to me – I mean the brain is analog. It’s not digital. So sometimes because say well, how can anything learn if there’s no microprocessor, right. That was the proof. You could learn. It was all analog electronic circuits that they had on the robot and it was brilliant how it worked. It was also very fast. There was a lot of interesting emergent behaviors. It was about this big, the robot. He had it in an arena. He reproduced the experiments by the biologist. You know the biologist they put up these landmarks, when the ants come out and then when they come back they remove some of the landmarks and they look at the kinds of errors that they make and he could reproduce all of these errors with this robot. That was a landmark thing so I think Franceschini. But anyhow coming back to vision I think optic flow is extremely important. Also Dario Floreano at EPFL he builds airplanes, flying robots that largely navigate based on optic flow and they’re extremely fast and robust. That’s also I think that Floreano is doing is also very fascinating. Anyhow, so we started pursuing this optic flow and then got in contact with Srinivasan through Wehner, the ant biologist. And then that fitted the story with Turvey and that movement also in humans, movement and in the periphery like movement perception is very important. We started looking at movement and we saw there’s this field of active vision that had been around for a long time. So that through movement you actually generate sensory stimulation and that is one of our important principles of embodied intelligence is that every action – it’s actually not new, every action has a consequence in terms of patterns of sensory stimulation. I grasp a glass. That has visual consequences because I see the hand. The object also moves if I pick it up. I have proprioceptive sensory stimulation and I have haptic sensory stimulation in the hand and that is produced through my action. I’m not passively sitting here like a computer. That’s one of the fundamental differences to a computer. A computer is just passively sitting there waiting for someone to push a button or for some input. So it’s not input processing output but it’s we perform an action, the action has consequences in terms of sensory stimulation. Now, I said before, this is not knew. That’s actually we could trace it back to John Dewey the pragmatist and it’s a paper, a famous paper published in 1896 called, “The Reflex Arc Concept in Psychology.” And then there is, of course, Maurice Merleau-Ponty who was at some point very fashionable, the Belgian philosopher who said very, very similar things and then people like Aloimonos, they also came up or <inaudible> Bergi, they came up with similar concepts of active vision that actually the action is the important thing and we started looking more at that. Now, I don’t know whether I can tell you an anecdote. 

Peter Asaro: 

Please. 

Rolf Pfeifer: 

In 2009 I was in Shanghai Jiaotong University where we started the Shanghai lectures project, and there was a young lady and she was in vision, computer vision. And then she came to me, I started talking to her, she came to my office. And then she said, “Yeah, that’s what you’re saying is actually interesting.” She asked me some things. I explained it to her. And then she says, “Yes, but you’re not solving the partial occlusion problem.” And I said, yes, that’s true, but maybe if you think in terms of autonomous agents, or biological systems they can move. And so maybe when you’re really trying to solve the partial occlusion problem from static images you’re maybe trying to solve the wrong problem. Think about a biological system, think about embodiment, an embodied system can move around and then maybe or you can sort of just into this you have a cluttered table and then you could just with your hands you get into the cluttered table and then it’s obvious what the objects are that are on the table. So maybe you need to solve a different problem. Initially, it may seem that the problem gets more difficult, but maybe the partial occlusion problem is really an artifact of this particular approach to vision. And I think in many cases – so that was kind of the philosophy that I’m trying to sort of communicate, you know, think differently about your problems. 

Peter Asaro: 

Great. To what extent do you think that that sort of thinking has started to permeate more of the robot vision community? 

Rolf Pfeifer: 

Well, I think, the – I mean we have to be clear that the vision community, classical vision community in some respects has been very successful. Also, I mean robotics, traditional control engineering manufacturing has been enormously successful. And so I think still by far the largest part of the community is actually traditional like that in that sense. However, many people now from traditional robotics – I call it traditional robotics. I don't know what to call it but I could say manufacturing, or they started realizing that there are limitations even in the manufacturing domain. I was just at the ICRA conference recently and there is an American company Adept and they are into, among other things, they do many things, but one of the things they do is food handling. Now, if you have, for example, baked goods or if you have fruit or as a Swiss I would say if you have chocolate they have an enormous variation of different kinds of shapes. They’re confronted with – one of the reasons traditional manufacturing works so well is that everything is predictable. So basically you can program the movements down almost to the last detail, right. And then you can use powerful optimization techniques and it works you have these powerful motors. They do what you tell them to do. And now when you have different shapes, so you have a certain level of unpredictability in the system. I mean in the real world you have unpredictability which is why you need all of this soft robotics stuff in the real world. In the manufacturing environment you don’t have this unpredictability, this uncertainty. You can program the things. But now if you deal with food which has these unpredictable shapes you need to think differently about it. And that reminds me another anecdote that I’m sure Hod Lipson will tell you. Jaeger in Chicago and Lipson in Cornell they built I think it was done about a year or two ago, that’s for me one of the big highlights of soft robotics, they built a coffee balloon gripper. I don't know whether you’ve heard about that, the coffee balloon gripper. Basically, his story and it’s brilliant I saw the videos. The videos are on YouTube. It’s brilliant. So he says, well, you go to the supermarket and you buy a pack of ground coffee and it’s hard like a rock. You open it and then it gets really soft. So what they did they took a balloon, they put ground coffee, finely ground coffee into it and tied a mechanism for applying a vacuum. And so basically what the coffee balloon gripper does it goes over any kind of object of any shape, of any size, of course, not a huge object but of any size the gripper goes over it and then it passively, because it’s soft, it passively adapts to the shape of the object. Then you apply the vacuum, the structure hardens but doesn’t change shape and then they can pick up any object with exactly the same control. They don’t need to know anything about the object and I think it’s brilliant. That’s to me the illustration of soft robotics. 

Peter Asaro: 

Using coffee grounds <inaudible>. 

Rolf Pfeifer: 

That’s right. <laughs> The coffee balloon gripper is really fascinating. 

Peter Asaro: 

Are there other anecdotes? What was it like working with Luc Steels? What kinds of things did you learn working in his lab? 

Rolf Pfeifer: 

He has a background in language. I think he has a Ph.D. in linguistics from MIT. What I found interesting is that he was really exploring at the time, I think. It was an exploratory phase, I think, for everybody. It was very exciting but we all didn’t really know where we were going. And Luc Steels he was exploring artificial evolution. And he had a number of people working on artificial evolution doing reviews of genetic algorithms and all sorts of things. And so basically I learned about artificial evolution there. It’s one of the things I learned. He was exploring vision. He had a fellow from France, I forget his name. He was doing vision together with John Hallam biologically inspired stuff. And he invited the roboticists so he basically started this up. He was cooperating with David McFarland trying to build and then they built this like I thought – also thought that was a brilliant idea, this artificial ecosystem because McFarland they were both interested – that’s one of the things I learned from Luc Steels, one of the really big things. I think it was he who coined the term designed for emergence. And then at the time we didn’t really know that but now I think we understand it much better every behavior is emergent. You cannot program a behavior into the system. You need the physical body and the minute you have a physical body you have an interaction with the environment. Even, you have these manufacturing robots ABB, Swiss Precise, Swiss product. You tell the motor to go to a particular position. It will go to this particular position, right. But maybe you should ask the questions. I mean we organized – I think that was in ’95 we organized in conference in Switzerland on Monte Verità, the mountain of truth, and it was called “Practicing Future of Autonomous Agents.” And that was really a fantastic conference. Everybody had to take a robot and there was a lot of hands on work and everybody was here like Rodney Brooks, I think Maja Matarić, Tim Smithers, also Daniel C. Dennett and Gregor Schöner. We had everybody who was really working in this area. And there was a special issue of robotics and autonomous systems about that. So that gives basically a perspective of what we thought about this at the time. 

### Swizz Robotics Community

Peter Asaro: 

Great. What’s the sort of relationship the various institutions working in robotics around Switzerland, the University of Zurich and ETH and EFPL? 

Rolf Pfeifer: 

Okay. It used to be the case that we were doing our own thing. Actually, for a long time we have been working with the people at EPFL with Auke Ijspeert and Dario Floreano. And we’ve had several projects together. Now, we haven’t been working a lot with the people at ETH Zurich until recently. And so Dario Floreano and myself we started an initiative for this National Competence Center for researching robotics, this NCCR robotics. Probably people told you about this, right. And now I’m really surprised in this project people from various disciplines they actually cooperate. And others, for example, Roland Siegwart he was involved in more let’s say traditional robotics but now he’s really doing pushing this dynamic movement, business and he was all in favor hiring Fumiya Iida who is a former Ph.D. student of his laboratory and then worked with Russ Tedrake who was also at this workshop but ETH now. But Russ Tedrake was working on under actuated systems or is still working on under actuated systems. And now this is a big research topic in Roland Siegwart’s laboratory. I think the interest is definitely there. And all of the people who are now in this project which is about 20 research laboratories in the field in Switzerland they all cooperate one way or other. I think I’m very happy about this. 

### Ph.D. Students

Peter Asaro: 

You just mentioned where one of your students went, but who have been some of your other Ph.D. students and what kind institutions are they now? 

Rolf Pfeifer: 

Right. I recently – I think about 12 of my former Ph.D. students or post docs there are now professors at various institutions. Fumiya is at ETH. Rolf Miller is in Bielefeld doing bio-robotics, biologically inspired robotics. Another Ph.D. student was working more on situated cognition. He’s now a professor in Australia. One Ph.D. student was really brilliant. He also got the, what is it called? The Apple Design Award. He developed a software package and he got the Apple Design Award and then for me, unfortunately, started working for Apple after his Ph.D. because he was a brilliant researcher. What are some of the others doing? One former Ph.D. student she was also working on biologically inspired robotics with Wehner and then with Luc Steels and she’s now a professor in Berlin I think at the Humboldt University in Berlin. I think one Ph.D. student who was working more on neural computation and models of that kind is now working for the pharmaceutical industry in Switzerland. Paul Verschure. He was a psychologist and got his Ph.D. here and now he’s doing a lot of neuroscience. He’s also involved in this flagship project. He’s a professor in Barcelona I think for neuroscience or computational neuroscience in Barcelona. There are more. I would have to look them up. 

### Future of Soft Robotics and Bio-Robotics

Peter Asaro: 

What would you say are the big outstanding problems and future goals for soft robotics and bio-robotics? 

Rolf Pfeifer: 

Okay. I think one of the – I think there are many goals. Of course, let’s say one of the goals is this robot companion project because I think it will incorporate all of the hard scientific issues of trying to build an intelligent system. And because it’s such – see there are six projects that are currently being evaluated or that are currently set up or proposed that have been preselected from about, I think, 30 or 35 submissions. Six have been pre-selected. They each get 1.5 million euros to prepare a proposal and the robot companion is one of these six and they will fund two of these six. Whether we get the money or not we don’t know. But in any case, I think this is really, for me, a brilliant exercise because of the community building effect that the whole thing has. Never in the past have so many people and so many very bright people been cooperating so closely on setting up this project. Sometimes I get the feeling it’s a bit like putting a man on the moon sort of thing where there’s a lot of excitement and people really want to cooperate from various disciplines. So I think this is in a sense, even if you don’t get the money, this is a historic event in that way. But this is the formal framework. I think for me one of the really interesting questions that I would like to – let’s say practical questions and then there are theoretical questions. Now, in terms of practical questions Foxconn is the company the produces the iPhone and the iPad for Apple. And the production is outsourced to China and they had troubles with working conditions. They were in all of the newspapers. And the big question for me is what is it about these manipulation tasks that the humans do in these factories that make it difficult to automate these tasks using the known manufacturing technologies? If it were easy to do they could do it in I think it’s a Taiwanese company, in Taiwan or they could do it in the U.S. or in Europe somewhere where they wouldn’t have to worry about the working conditions. But there’s seem to be factors that make it still cheaper to outsource it to China even though now the sellers increased. The one child policy is beginning to have an effect. And they demand better working conditions. What is it about this? So I think we need to really look at this. And then I think we could augment, increase, the level of automation by an enormous amount. And some people like Rodney Brooks at Heartland Robotics and others they think that we’re into a second industrial – not a second but another industrial revolution with I don't know whether Heartland is really working with soft robotics. But looking at this manufacturing and for me it’s really the soft stuff. Adept, for example, is looking at soft grippers, you know, that passively adapt to shapes and things like that. That’s going to be a big challenge. How can we augment the level of automation so that we can re-insource this production to Europe or to the U.S. or to the home countries and don’t have to rely on this increasingly unreliable resources and expensive resources. That’s in terms of practical applications. And I think it will happen. And for me a large part of this will be materials and soft robotics. Now, what are the theoretical issues? If I look at – what I would like to understand, of course, we are a product of evolution. For example, I stand I let my arm swing back and forth and then I encounter an object with a hand. This movement with the arm is actually a very complicated movement in 3D space but the control for it and the energy requirements are very, very simple, very low energy requirements. It’s a very natural movement, much more natural than kind of making a movement like this. But this is also much more useful because I encounter an object well than I grasp it. I don’t grasp it like this but like this. And then I grasp it and as we said before you generate sensory stimulation in different sensory channels. And then you can start making predictions just by looking at it by simply associating it. While you’re grasping something you are inducing correlations in the patterns of sensory stimulation in different sensory channels individual, in the haptic and in the proprioceptive. And these correlations are produced through the physical interaction with the environment. That’s the embodiment. Now, you can have a very simple heavy and learning mechanism that just sort of picks up the correlations to make predictions. By looking at object you already have an expectation of what it will feel like when you grasp it. Now, that all depends on – so basically you have a motor signal that’s being sent to the muscles. This motor signal is used to make a prediction about the expected sensory stimulation. Well, that, of course, what you have learned depends on the morphology, on the distribution of the sensors, on the organism. You know the eyes you have here, here you have high – this high density of sensors on the hand. I mean if you want to know about an object you take it into your hands, you feel it. You don’t rub it against your back, right. That’s because of the distribution of the senses. And then the motor signal only makes sense in the context of a particular physical system. You know, you have the same motor signal in two different physical systems. They will behave completely differently. Now, we get this sort of how everything works together. I have a motor signal. I have a particular morphology distribution of sensors. I have preferred trajectories because of biomechanical constraints. And then certain depending on the action the patterns of sensory stimulation that I get are also going to be different and they depend, in turn, on the distribution of the senses and, of course, also on the objects and the environment. Now, I’m looking for a theoretical framework in which – now intuitively – I mean you have been nodding now all of the time, so intuitively I think it’s very plausible, right. Now, what we’re lacking at the moment is a theoretical framework that we can really use like control theory. I mean that’s somehow the goal that we have a real framework. I don’t know whether it’s going to be like control theory in which we can theoretically describe all of these concepts and how they fit together. We have a project, a big European project now called ESMC extended sensory motor contingencies. This is all about sensory motor contingencies. And we’re also interacting closely with J. Kevin O’Regan. He is a psychologist and he came up with this concept of sensory motor contingencies and he is interested in qualia. Qualia means – it’s for a long time been a big philosophical issue. We have different sensors. We have vision. We have haptic sensors. If I look at you why do I know that I see you when I don’t feel you with my hands, right? Because everything is just neural pulses in the brain. It’s just neural pulses but I know that I hear my voice now. I can see you and I can feel my knee here, right. Why is that? And so Kevin O’Regan and that goes very much into this theoretical framework. He says it’s because of the different contingencies. So basically the signatures of the patterns of sensory stimulation from the visual system when you move, when I turn my head, the visual stimulation changes in a particular way. This is very different. This pattern of change is very different from when I move my hand over an object and feel it. The signatures are very different or it’s very different from what I hear. In hearing the movement doesn’t play such a big part. And this, to me, is about sensory motor contingencies and these are the big issues. And what I’m interested in how the materials, how all of the morphologies and morphological factors and the control, the motor control how this all plays together. I want to make basically this big story. 

Peter Asaro: 

What about the integration of this as well. 

Rolf Pfeifer: 

Yeah, that’s a very big issue. And that I think we need to understand. And I sort of – many people think about hierarchies. I really think – I’m sort of a dynamical systems person. That maybe also relates to the fact that originally I’m a physicist and I don’t like to program hierarchies into systems or to build hierarchies into systems. I think hierarchies should be emergent. And so basically we should look at all of this and with this robot what, for example, my post doc Hugo Marques is doing is looking at emergence. How can you get behavior as emergent, rather than having to program them into the system? This is, again, back to Luc Steels’ statement, design for emergence. Every design has to be for emergence. I think this is the big issue. Yasuo Kuniyoshi at the University of Tokyo he’s one of the big champions of emergence. 

### Advice for Young People

Peter Asaro: 

Great. A wrap up question, for young people interested in pursuing a career in robotics or getting involved, what sort of advice do you have or them? 

Rolf Pfeifer: 

Well, that’s a good question. I’m very interested in interdisciplinary research. In this flagship project we have neuroscientists. We have people from biomechanics. We have materials scientists, electrical engineers, computer sciences, we have everything. We have psychologists. I really believe in interdisciplinary work. I also believe that you need a firm grounding in one discipline. I think studying – you know, studying if you can and if you have pleasure in doing so I think theoretical physics, you know, is a good thing because it sort of – I mean it’s just thinking about things. It’s difficult. You get the mathematical tools. And then from there you can do anything. For example, most people in computational neuroscience are theoretical physicists. And so you can go into engineering very quickly. I think you can just learn things very quickly. So if you choose something like mathematics, physics can also be engineering but I think it should be one discipline. It can also be biology. Then it sort of can be neuroscience. But I think you should have sort of something like a home discipline and then you can open up to an interdisciplinary work. And then you can just join any kind of project. And I think if the person is in Switzerland then I think this National Competence Center for Research and Robotics really provides all of the opportunities that you can potentially think of. We are also very connected with everybody in the world with U.S. universities, with universities all over Europe with all of our European projects. But also we have very good contacts in Japan, many universities in Japan and China. I think really you have all of the opportunities. And it’s mainly the disadvantage of a small country that you don’t have the talent in the country itself. You have to be internationally connected. I think the research seen in Switzerland is probably one of the most international in the world. 

Peter Asaro: 

Great. Is there anything else you’d like to add? Anything we missed? 

Rolf Pfeifer: 

Well, it’s hard to say. There’s so many things. I think everything is important. No, not really at the moment. I think that’s fine. Thanks. 

Peter Asaro: 

Great, thank you very much. 

Rolf Pfeifer: 

Thank you. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Rolf_Pfeifer&oldid=203599 "
