1 Herman Bruyninckx 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 FIRST Robotics Project and Challenges 4.3 Open Sources Libraries 4.4 SECOND 4.5 Robotics Collaborations 4.6 EURON 4.7 Challenges of Robotics 4.8 Other Projects 4.9 Future Applications 4.10 Advice for Young People 

## Herman Bruyninckx

Herman Bruyninckx was born on December 22nd, 1962 in Turnhout, Belgium. He attended Katholieke Universiteit Leuven (University of Leuven) in Belgium, completing three master's degrees: Mathematics in 1984, Computer Science in 1987, and a postgraduate engineering degree in Mechatronics in 1988. He completed a short period of military service from August 1988 to July 1989 before returning as a research assistant at the University of Leuven in the Department of Mechanical Engineering from 1989 to 1995, when he earned his Ph.D. there. He continued to do research with organizations such as the Fund for Scientific Research-Flanders (FWO) in Belgium, the Robotics group at Stanford, and the Centre for Autonomous Systems at the Royal Institute of Technology in Sweden. Further involvement with the robotics community includes membership with European Robotics Research Network (EURON) in 2000 and becoming its coordinator in 2007, and initiating the Free Software project, OROCOS in 2001. 

Continuing at Leuven, Bruyninckx became an Assistant Professor in 1998, an Associate Professor in October 2003, a Professor in 2008, and finally a Full Professor in October 2013. Additionally, he became a part-time Full Professor at Eindhoven University of Technology in February 2014. His involvement with the robotics community focuses on mechatronics, robotic programming and control, sensors and perception, and learning in a real-time environment. 

In this interview, Bruyninckx recounts his career and his contributions to the field of robotics. He discusses past projects and the challenges that roboticists faced and will face. He reflects on the future of the field and its applications, and provides advice for young people interested in robotics, stressing the importance of a broad, multidisciplinary scientific education. 

## About the Interview

HERMAN BRUYNINCKX: An Interview Conducted by Peter Asaro, IEEE History Center, 8 July 2011. 

Interview #690 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers, Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Herman Bruyninckx, an oral history conducted in 2011 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Herman Bruyninckx 
INTERVIEWER: Peter Asaro 
DATE: 8 July 2011 
PLACE: Leuven, Belgium 

### Early Life and Education

Peter Asaro: 

Okay, can you start by telling where you were born, where you grew up, and went to school? 

Herman Bruyninckx: 

Yes, so I was born in a small town in the northern part of Belgium close to the Dutch border. And I had an eventless youth. So, I went to primary school and high school. It turned out I followed the more scientific oriented curriculum. And until I was about twenty-three or so, I just did the same thing as my older brother did. So, I studied mathematics here at university. And after that, I did the math degree in computer science. And during my master’s thesis there, I did some work on the robots here in the mechanical engineering department. And that got me interested in robotics. And I followed a post-graduate master in mechatronics, which doesn't exist anymore. But that was twenty-five years ago. And that was a perfect preparation for a Ph.D. in robotics. So, I started my Ph.D. research here in '88 at this department with professor De Schutter, who was a Ph.D. student himself of Hendrik Van Brussel . So, I'm a third generation of robotics research here at the department of mechanical engineering in Leuven. 

Peter Asaro: 

What was you master’s thesis on? 

Herman Bruyninckx: 

So, the – well I did three master's theses. The first one in mathematics was on special solutions of the Einstein's General Relativity. I think the one in computer science was on interfacing a robot, an old IBM Skyway robot, through a serial line using then new technology of object-oriented programming languages Modula-2. And then my master in mechatronics was about interfacing a CAD system with a machine to a large machine to – in a company somewhere here in Belgium. So, these were already steps in the direction of my current research, which is combining software engineering with robotics. That's the core of my research, this combination, so working towards better software design but for mechatronics and robotics systems. 

Peter Asaro: 

And why did you shift into robotics from physics? 

Herman Bruyninckx: 

It's by circumstances because you meet people. And then when I did my master's degree here, my later supervisor was also my thesis supervisor at that moment. And it just happened to be that he had the European research project in robotics starting around that time for which he was looking for people. And that's how you roll into a certain domain that you had no idea, or no ambition for before or during your studies, so by accident. 

### FIRST Robotics Project and Challenges

Peter Asaro: 

So, your first robotics project was the SCARA robots? 

Herman Bruyninckx: 

No. My first robotics project was called FIRST. It was – the acronym stands for Fundamentals of Intelligent Robot Systems. So, twenty-five years ago, this project basically thought to solve the problems that we are still solving now. It was about integration of vision and force control for assembly like kind of operations. So, these are problems that are still not solved nowadays. But at that time, we didn't really know exactly what the problems were. So, that was the first research project. And I was also – that's a European research project. And nowadays, I'm still heavily involved in European robotics research projects, not just as a researcher, but also in my role as the coordinator of the European Robotics Research Network. I'm also looking at the other side, helping European commission by putting some research questions on the agenda and trying to motivate why European Commission should from this kind of stuff. 

Peter Asaro: 

Let's come back to that and start with your research a little bit more. So, what were some of the biggest challenges that you've seen in the integration of vision and force control from obviously your technical perspective? 

Herman Bruyninckx: 

From a technical perspective, the thing that we've underestimated, everybody's always underestimating and still underestimating, is that we as human have so much knowledge that we use in making decisions or interpreting what is going on, so much of this implicit knowledge that our robots or computers do not have. So, in order to make an intelligent decision, we're using a lot of knowledge. And we bring knowledge together that we, at this moment, we have not encoded in a formal way. So, there's no way our computers, let alone our robots, can make use of this knowledge because it's not there in a form that they can use. Earlier today, I was in a workshop here where we are working towards the ontology of robotics. That's basically meaning that we want to put structure in all the knowledge that the robot needs, how the different kinds of knowledge relate to each other, and how you can represent them in a formal way. This is a huge undertaking. It's a lot of things that are so obvious for humans that humans don't even think about these things anymore. But they are not at all obvious for robots. And that's over the twenty-five years of having in robotics research. That's the recurring problem. And we always find out that we need more and more knowledge to be integrated. So, that's the major problem that I see in the last twenty-five years of robotics, and also the current twenty-five years, I think. 

So, there's a lot of progress being made in the subdomains, making machines like mechanical devices, making controllers for them, making them cheap and robust. That's rather mature. We can do a lot of computer vision things. We can do impressive things in AI. But bringing together to solve problems with robots, we need a lot more integration because the kind of knowledge that people are using in AI to solve AI problems is not at all or only partially relevant to robotics problems. So, that's the kind of missing gap, the integration between subdomains that by themselves have matured a lot. The integration is still a major problem. And it also works in two directions. By doing – trying to solve problems with robots, we find out that people have only – let's say in the mechanical engineering domain, or in the control domain, they've only solved a part of the set of relevant problems for that domain. So, the kind of robot you have here is seven degrees of freedom robot that's more than just controlling seven motors. The fact that they together form a robot device, and it has a certain task, brings in new challenges also for the fundamental scientist like control, or AI, or just software engineering because a modern kind of robot system will have the robot itself, but also half a dozen sensors, dozens of planners and things like this. The computational power to compute everything we have to compute is not possible on one single PC anymore. You have to bring together a dozen other computational units, from very embedded ones, FBJs, to desktop PCs. And also there-there are software engineering problems that people in software engineering, computer science, have not yet solved because they were not relevant. Or they just didn't think about these problems. So, there are a lot of hard real-time problems. There are also coordination problems, which piece of software do I want to run before another one, and things like this. Also, there is a lot of knowledge and engineering that is still unsolved. 

### Open Sources Libraries

Peter Asaro: 

You've done some work in the open source libraries on these kinds of utilities that could possibly aid in – 

Herman Bruyninckx: 

Yeah. So, I think I was the first one in robotics and also much broader than robotics that decided to make open source an important part of my academic research. I still remember very well November 1st 1998. That was the date I decided I'm going to take this open source that – I was using it for a long time already. But I'm going take this serious and do research about it. And I'm going to use it in my research, but also using it because it fits very well to research. So, research is about sharing results and improving about each other's findings. And at that moment, it was not done in robotics or mechatronics or control. So, I said in order to make better progress in robotics research, together with the fact that software is becoming an ever more important part of robot control systems, I decided that the open source way is a very important way to foster the research. Ten years ago, I started with the OROCOS project. That was meant to make open source software but for industry. The project was triggered by three companies here in Belgium, not robotics companies, but machine tool vendors that were confronted with limitations of the control software they could buy from companies like Siemens. And so, they came to us. And they said, "Okay. We know that you're doing something on open source. Can't we do a project together to fulfill our needs?" And out of that there was a stimulus to start the OROCOS project. So, from day one that was driven by industry, paid by industry to some extent, and also licensing and development scheme that is industry friendly with some of these also very relevant performance issues relevant to industry. So, OROCOS is still focusing on real-time performance and this kind of stuff, which a lot of the older open source projects that you now see on robotics are not focusing on. So, we still have a niche there which differentiates that project from others. But in the meantime we combine the OROCOS project with a lot of other open source projects because you need a lot of functionality. 

Peter Asaro: 

So, what were the core functionalities that you started with and what have you built up around that? 

Herman Bruyninckx: 

So, OROCOS is still a niche project. So, it wants to be the best one in what we call hard real-time component-based software. So, you have different components because there is different functionality. Or you have different computers that you have to connect. And the OROCOS project focuses on making all these things hard real-time safe to allow people to get the last piece of performance and determinism out of these things. So, that's only a small part of what you have in the robot system. So, OROCOS does not provide everything that you need in a robot, not at all. And this project also doesn't want to do that. It wants to be the best in this niche. So, nothing has changed in ten years with respect to that goal and these ambitions. We are improving in quality and also in breadth of platforms we support. And recently the big, new drive is in providing better tooling to help people to use the software in a more easier way or more robust way. But the core ambition and core functionality's still the same, hard real-time systems. 

Peter Asaro: 

And do you see it as compatible with ROS? 

Herman Bruyninckx: 

It absolutely is. So, one of the – we are part of the PR2 beta programs. We have a PR2 robot here provided generously by Willow Garage. And the reason why it's here is because our contract with them is about the integration of the OROCOS hard real-time thing with a non-real time ROS community, which provides a lot of functionality. But their real-time control is not the focus. So, we have provided bridges between these two frameworks. And that's also part of my research, how do you make systems out of components that come from different vendors that were made with different objectives. That's also a research domain. So, it's not just putting the software together because you want to do something. It's also a research activity of mine. 

Peter Asaro: 

What are the biggest challenges in that kind of integration? 

Herman Bruyninckx: 

One of the major ones is lack of standardization. Other domains have gone a lot further in standardization than in robotics. If you look at let's say mobile telephony, yeah, you have the GSM standard. Or in the Internet, you have the HTTP protocol standard, or HTML mark-up language standard. In robotics, there's basically no standards at all. So, no two robot manufacturers provide programming languages for their robots that are interoperable with a competitor. No standardization at all. And also, something that's a bit surprising to me, also the open source projects are not interoperable. So it's impossible to connect whatever component you have in ROS to whatever component you have in OROCOS or somewhere else without a lot of glue code to be written to make these things work together. That's a bit of a disappointment. So, the open source community is not at all better in coming up with standards than the commercial robot manufacturers. 

Peter Asaro: 

Who do you think would be the appropriate group to try and establish those kinds of standards? 

Herman Bruyninckx: 

Well, there's – I tried several times already to start activities there, not just me, but also some other people. So, I think we are now in our third cycle of trials. But I think now it's going to happen. So, for example, in the last European robotics forum, that's the annual gathering in Europe of all European robotics stakeholders, there was a workshop on standardization. And some things are growing there. So, it's not just in Europe. We also have some contacts in Japan for example. And some things are starting now. So, there's recently one of the results is the establishment of the RETF, the Robotics Engineering Task Force, which is very much inspired by the IETF, so the Internet Engineering Task Force, which is a proven way of providing small standards, community-driven things. So, we are trying to adopt that model to also come up with standards in robotics. And it's very modest in its current aims. But I think something will come out of it. And we're now more completely thinking about how to standardize logging. So, when you get the information from your robots, it will be nice to have some kind of standard format of how you format log files. And the other thing is how do we present motion and velocity in 3-D space because a moving object in 3-D space is a core of robotics. And there's no standard representation for that. So, these are these little seeds that now there are some sub-committees, a group of people that are interested in doing these things. And it's very important. Robotics as a domain is very small, especially if you look at the industry. The robotics industry that's let's say order of magnitude one billion Euros or dollars a year. That's a very small industry compared to embedded systems, or telephony, or cars and so on. That's orders of magnitudes smaller. So, this industry is not able or willing to drive standardization. It's an industry that is using technology developed somewhere else and integrating it. And if you compare this to communication or a car manufacturing, these are industries that can really drive developments. If the car industry needs a new standard for a new fuel bus in their cars, they will drive it. That's not happening in robotics. They're using technology. So, industries are driving standardization. That's a problem in robotics. 

### SECOND

Peter Asaro: 

So, what were some other, after FIRST, what were some –? 

Herman Bruyninckx: 

The other project – 

Peter Asaro: 

Was there a SECOND? 

Herman Bruyninckx: 

There was SECOND, yeah. I came up with this acronym. It's basically trying to solve the same problems. I don't remember exactly what SECOND stand for, but something – I don't know anymore. So, yeah I had two European projects that basically covered my Ph.D. And then now, twenty years later, I don't know exactly, but I'm probably involved in my tenth European project or something like that. For me as a person, as a researcher, Europe has been extremely important. That's not the case for most of my colleagues here. But one way or another, I've been very much involved in European projects. And that's great. The research areas, the universities in Europe, they have integrated a unified Europe since a long time already. So, the rest of Europe, the political Europe is following a bit more slowly. But from a research point of view, this unification, it's already a reality since a decade or so ago. So, we really are looking at students at European level. And so, Europe is already reality, a big reality in academic research. 

### Robotics Collaborations

Peter Asaro: 

Who are some of the other European roboticists that you collaborated with? 

Herman Bruyninckx: 

So, as coordinator of the European Robotics Research Network I have a lot of contacts. And all of these are some form of collaboration. Of course the people you collaborate with in projects, that's a smaller subset, but in total will be about twenty five labs or so in Europe both in academia and in industry. Now I have projects running, by accident I think, with the two major European robot manufacturers, ABB and KUKA. It also happens to be two very complementary projects that I managed to use and to profit from as one bigger project. And also something that is rather new in this context is the increase in collaboration between projects. So, that's something the European Commission is stimulating lots, but also me as an individual, both as an individual researcher but also as EURON coordinator, something I'm proactively stimulating. And it's become a real reality. If you look again at the last European robotics forum, there were a lot of workshops organized by different projects and really finding out where the synergies are. So, that's a rather recent phenomenon. And that's a very good thing because until five years ago or so, research projects were islands. And they were doing something together as a partnership, and there were some results at the end. And that was it. But now a lot of projects start cooperating with other projects already in year one. And that's very nice. And also the European Commission is nicely stimulating this and providing facilities for that. They also provide funding for so-called coordination actions. They are basically not research projects in themselves, but money that facilitates research projects to do some things together. So, they have a nice set of instruments to stimulate cooperation. Currently, we also are in a very fortunate situation that is, over time spent of about five years, about five hundred million Euros investment from European robotics. That's a unique opportunity. Maybe it will never happen again. That depends on what are the results of the current projects that are running. But we're now really at a top of the opportunity graph let's say, a lot of money being put into robotics research, a lot of people doing research. So, there's now I think about forty to fifty projects active at this very moment in robotics. And we have never seen such a scale of robotics research in the past. Maybe we'll never see it in the future, but time will tell. 

Peter Asaro: 

I want to talk more about EURON but first I just wanted to clarify, what were some of the collaborations – influential collaborations that you had before you began here? 

Herman Bruyninckx: 

So, one influential collaboration, not in size of money, but in personal influence, was my first project there was a person like Mike Brady. He was at University of Oxford that was one of the senior people in robotics. And I didn't realize it at that moment, but that's the kind of people that give you vision and context, and direction in a natural way. So, these people say something, you have to do it like this or this because that doesn't work. And these are extremely good guidelines. It takes you long time to find out why they were right or so. But that's – from day one, I had this opportunity to work with people like Mike Brady. Also, here I had the opportunity to be the third generation. So, there is some advantage of continuity in research. So, that's another advantage that I only started to appreciate a lot later, so that is internal collaboration. Other interesting collaboration was the first European project that I got myself. That was also called OROCOS. That was with only three partners, with KTH in Sweden and LAAS in Toulouse. That was a very small-scale project. But the initial cross fertilization of these three groups is still living on. We are still working now in our research on problems that were identified at that time, ten years ago. And initial solutions that were provided at that time by this interaction between three different groups, so for me that's been a very important thing. Basically, that started my software engineering research in robotics. That was a very influential thing. But like most of these things, you only realize this long after the facts. 

### EURON

Peter Asaro: 

And then how did EURON come into existence and how did you become a part of it? 

Herman Bruyninckx: 

EURON, so I was not there at the beginning. So, my senior colleague Hendrik Van Brussel was one of the founding members of EURON. And EURON was an idea that was implemented and driven the first years by Henrik Christiansen who was then professor at KTH in Sweden. He's now at Georgia Tech in the U.S. And he is setting up similar kinds of things in the U.S. But it was a group of a dozen or so senior robotics researchers in Europe that got together and said, "We should do something to make more a community in Europe." So, I was not involved from day one. I was involved after a year or so of EURON. And then I was – first Hendrik Van Brussel was part of the EURON board. And then he gave me the opportunity to take his place. And that's how I got involved. And then when Henrik Christiansen moved to the U.S, then I became coordinator. But that took quite some time. So, I was not so ready to do it. But now I'm happy I did eventually. Yes. 

Peter Asaro: 

And how are you going about trying to build that community up? 

Herman Bruyninckx: 

So, the – I think EURON is a good example of how centralized funding from the EC can have a sustainable, long-term effect. So, EURON was a project funded by European Commission during eight years. And that money gave us an opportunity to set up meetings to build a network to try out some things that work and do not work. But since 2008 there is no funding anymore for EURON. There was a seamless transition from the funded EURON to the unfunded one, so now it's a community driven network that lifts, so it's not a problem to organize things. The network is strong enough to find organizers, to find participants, to find topics to discuss, so it's a nice example of something that was – they received money from the European commission and it's a sustainable thing. So in this respect I think it's a nice thing to be in. And also as a coordinator, to a large extent it's a self-organizing system, so I don't have to do so much things, like to give some ideas and bring some people together and do some practical things in the organization of the annual events and organize the Ph.D. awards, things like this. But that's not a huge amount of work because it's a transition that people know and understand and respect and contribute to by themselves. 

Peter Asaro: 

And how do you think the European commission decided to give 500 million Euros. How did that come about? 

Herman Bruyninckx: 

I don't know exactly. I'm very curious why, but I suspect that it's like many things that are going on at European level and I guess the same for the American senate and so on. So it's a couple of – or one or two individuals that believe that something has to happen and then fight hard to realize it. And I think that was one of the major reasons why this funding scheme was there. Currently we are working together with European commission to see how we could make a follow-up program of the same kinds – same scale or even bigger. So now I’m trying to help to get these ideas through. In the past I was just recipient of the result. I was not part of the creation, so I don't know the details. 

Peter Asaro: 

And within that do you see a certain emphasis on the kinds of projects that they're funding or the kinds of applications they want to support? 

Herman Bruyninckx: 

Yes. So there's definitely an emphasis and it's also an example of how political organization can give direction to research. The current program is not robotics. It's robotics and cognitive systems. So the politicians decided that it was important to bring the research in cognitive systems, or intelligence, closer to the robotics thing. And in the beginning I still remember a lot of people in robotics were afraid of this, but now I think after a couple of years that the program is running, everybody's happy with it. It's really been a synergy thing, not a them or us. No, it's a synergy. So that's a successful thing that was basically imposed on the community from the top. Of course European commission always listens to advisors and so people like Henrik Christiansen, others, gave these suggestions, but to most of the robotics community it was a bit of a surprise and uncertainty. But it's been successful. The potential is there and I see the enthusiasm of the robotics community that it's been a good idea. 

### Challenges of Robotics

Peter Asaro: 

And did you face a similar kind of challenge as a student interested in some of the more cognitive aspects of robotics and what is apparently a very industrially oriented program in chemical engineering? 

Herman Bruyninckx: 

That's one of the misconceptions. People think okay, I'm interested in cognitive aspects in robotics, so I'm not – I should not do anything with industry, and the other way around. That's not true. Even in the purest industry context, cognition should be a lot more prominent there. If you're making a better solution for a welding robot, for example, the progress is not in making a better robot but it's in better understanding, interpreting the process the robot is doing. That's cognitive science, so linking the perception with directions and interpreting what is going on and making the right decisions. That's equally valid and equally challenging in a very industrial context and in a more academic context of making, let's say, the artificial human, so a lot of the basic research questions are exactly the same. So that's one of my personal aims or ambitions that I can bring in this idea a little bit more in the community that there's a lot of interesting fundamental research to be done together with industry. 

Peter Asaro: 

What do you think are the biggest challenges facing the European network of robotics or robotics in Europe in order to get everybody together? What are the rules? 

Herman Bruyninckx: 

And this point it's not at all a problem of bringing people together. What I expect is a possible problem is that robotics, it's not a science in itself. It's a science of integration. That means for robotics research, you have to bring in more and more other sub domains. You have to bring in computer vision, you have to bring in AI, you have to bring in mechanical design, you have to bring in planning, and all these things. So I think that a problem is that the amount of competences, expertise and components that you have to bring in has become so large that no student can understand them anymore. That's something we see appearing already now. So new Ph.D. students in robotics are almost never Ph.D. students in robotics. There are Ph.D. students in some part of robotics and most of them have no idea what is required to solve – to make a complete robotic system, or they have no idea where their research can contribute to the full system, or what other research in other parts of robotics or other neighboring research domains, which of these research results are relevant today's research. That's a problem I see occurring now. The amount of knowledge has become too large, so I see a lot of students reinventing wheels that I know have been solved already 30 years ago, but in another part of robotics they are not connected to, or in another domain they don't know anything about. One of the big examples I learned recently, last one or two years, is that you have the concept of iterative learning control in the controls community, which is exactly the same thing if you look at the algorithms and the solutions as reinforcement learning in AI. These are two different communities. They don't know about each other. They're solving the same kind of problems with the same kind of technology but they are not profiting from the cross-fertilization. 

So the problem is how to make a robot learn how to move better. That's exactly the same thing as a controls engineer wants to make the same machine move better. There are some differences in what better means, so the performance issues might be different, but the techniques, the approaches, the problems and the solutions are the same. So these are two sub domains of robotics. They don't know about each other at all. And there are more and more of these examples that people used to look at or put in the same place that are now in different place and these different students don't meet each other anymore. Something we're aware of and it's something, as a UN coordinator, that's one of the important things I want to realize, to make sure that these bridges are rebuilt again if they have been lost. 

### Other Projects

Peter Asaro: 

Are there are specific projects that you've worked on in the last couple of decades that you want to discuss? 

Herman Bruyninckx: 

Yeah, one of the interesting ones, recent ones that at first sight were a complete failure, but in retrospect we're extremely similar, was the RoSta project. So I was not a partner in the RoSta project itself, so that was a coordination action. RoSta's standing for Robotic Standards. It had a very ambitions goal to create reference architectures of robotics, ontology of robotics, the structure of the knowledge, and all of these kind of stuff. The hope or the expectation was that they would come up with some solutions in the three years that the project was active, but at the end that was not at all the case. I was there as an expert a couple of times, but that project has now created the insights and the networks of researchers that are now tackling some of these problems in more detail. So that was one of these projects that was a failure at first sight, but a godsend afterwards because sometimes it needs people or communities need a lot of time to understand what are the real problems we have to solve or to understand how big a real challenge is and that was one of these examples, the RoSta project. 

Peter Asaro: 

What were some of the reference structures that you tried to build? 

Herman Bruyninckx: 

That's a good question. People have been making robots for years already. People are, let's say, the challenge of driving around a robot or autonomous car without colliding in a decently robust and optimal way to drive from A to B. That’s a solved problem, or I feel that's what is achieved there. But there's still no – at least as far as I know. I've never seen the reference architecture or the cookbook, the recipe of how do I design such a system. And if I change this and this part of the robot or of the task, how should I make a variant of the existing system so it can solve these things? So there's something lacking in consolidation of all this research. We have built systems that work, but we have not yet consolidated this knowledge into something permanent that we can teach to students and say oh, intelligent cars, that's how you do it. And these are the problems that are still unsolved or the things that's changed from system to system or from application to application. We're not there yet. That’s a bit surprising. Also we do not have any instruments to stimulate this, so writing papers on systems or consolidation of knowledge, very difficult to get those published. There are no journals about it. It's not what we engineers typically evaluate or say, "Okay but that's not new; it has been done already." But it's an important thing, so consolidate your knowledge in best practices or working designs. Very few people do that. 

Peter Asaro: 

Another issue that has come up here is the safety of robots, especially as they become more and more engaged in human interaction and human environments. And I just wonder what your thoughts are on how it might build standards. 

Herman Bruyninckx: 

I'm part of the Rosetta project, and the Rosetta project is basically two complementary sub project, and one important half of the project is indeed in preparing the future norms, standards in safety 'cause they're not there. So the fact that you bring out the roles out of the fences and in contact with humans, physical and emotional interaction with humans, and then Rosetta is focusing on the physical interaction. That's not an easy thing to do. There are also a couple of other European research projects, France and so on. So we are now learning as a community what are the relevant things that should end up in a standard and what are possible ways that the standard could look like? Also an important issue in this concept that the European commission has brought in the community is ELS: Ethical, Legal and Societal issues. That's something that no Ph.D. student, no researcher was really considering seriously or didn't even know about. But now all the projects have to consider ELS issues. It's something that the commission brings in because that's the first step towards safety standards or ethical standards so bring in the – or pointing the researchers to these topics that they are also important. So that started a couple years ago. Everybody now knows what ELS stands for; that's the first step. And some projects are focusing on trying to do something there and it's going to be important but we are just at the beginning of understanding how to do that. 

Peter Asaro: 

What do you think are the big issues as far as the actual ethical, legal, societal issues and what do you think are the challenges for getting academics and industry in Europe to find a solution? 

Herman Bruyninckx: 

That's a very difficult question. I don't know if I have a clear answer to that. I have some observations and I suspect that the ELS issues are not the same for sub domains in robotics. If you're in surgical robotics, you would expect that ELS issues are the most stringent, but that's not true because if a surgeon decides to use a prototype robot and he says okay, I sign for all the consequences that can occur because of the use of this device; then you're done, roughly speaking. On the other hand, an industrial robot manufacturer, if, for example, ABB robot is being used in an application and an operator gets hurt or killed, then this automatically reflects back on the image of ABB, even if it's probably not their fault, so the problem is somewhere else. So there the ELS use is a lot more strict or they have a lot more consequences than in surgery, things like that. It's a very strange thing because the perception of people is very important and that also means that people are accepting different risks of the same device in different contexts. So this same robot, when used as a surgical robot, would cause a lot less problems than using this robot, for example, in your home to try to do your dishes because if there this robot breaks your dishes then you can be sure that people will claim reimbursements from the manufacturer; while if it happens in a research environment or in a hospital, that's the cost of doing – of using the devices. Perception is a very important thing. And people put a lot of perception in the system, in the machine, depending on how it looks like, or how it is called. So calling something a humanoid robot, that gives a lot more expectation, perception in the humans than calling the same device a tree-structured robot, and it's a valid name. Human structures or humanoid robots, they are structured in a tree structure. That's basically what they are: Devices with a kinematics like a tree that can move. And that's a lot less fancy and a lot more down-to-earth than calling it humanoid robots. But this name makes people think that these devices can do a lot more than they are capable of and that influences also the ELS issues because if you give the device a name that looks a bit industrial or so, then people say oh but then you'll have to have certification and so on. Well, if you say it's humanoid robot, it's a human friendly device, and people will go out and touch it and interact with it while the device is exactly the same device, equally dangerous or not; but the name is so important. And the name also, that's important in the people that do the legislature eventually. These are not engineers. These will be lawyers or other kind of people. 

### Future Applications

Peter Asaro: 

What do you see as the big up-and-coming applications for robotics? 

Herman Bruyninckx: 

Oh, if I knew I wouldn't tell you because that will be probably a billion, a multi-billion Euro market. So I don't know. But I have some ideas, so the concept of a robotic app platform, that's – everybody talks about that, so the concept has proven to work with smartphones and so on. So in principle it could also work for robots. That means now if you buy a robot as a company, you also buy the applications from the vendor or from the integrator, while in principle nowadays it could be that you buy an app from an independent third party on your robot. That's a business model that is going to happen one way or another. It does not exist yet, because it needs some time, but that's something I see happening. That also means that the robot manufacturers have to open up their senses a little bit more, so that's a third party can indeed make an application there. But that's an evolution that's going on, so all the robot manufacturers are now already providing or working on interfaces to their systems that are a lot more open than what they used to have in the past. That's something I expect as a kind of market. Which applications will be the killer applications? That's difficult to say, but that's an evolution I see, so kind of app market. So the important thing is third parties making applications for the robots. 

### Advice for Young People

Peter Asaro: 

What kind of advice do you have for young people who are interested in a career in robotics? 

Herman Bruyninckx: 

How young are you thinking of? 

Peter Asaro: 

High school. 

Herman Bruyninckx: 

High school. Then high school kids I would never say that there's a career in robotics. Robotics is not a big enough domain. It's a science of integration. So I don't see robotics as an end point of a career or an ambition of a career. No. Because it's so complex and it's so versatile, so I think the traditional engineering, master's of engineering are fine. Robotics will come later. I would not support – I'm not so positive about having a master's in robotics. I think that doesn't make too much sense because robotics as a science of integration requires you to have expertise in other sub domains before you start applying in robots. I’ve seen many places, especially in computer science schools, where they bring in robots and say okay that will stimulate people to – for social engineering and so forth. But if I then look at the results, the results are awful. They are learning wrong things. So they want to solve the robotics problems as an example of object-oriented design. That doesn’t work because robots are a synchronous, concurrently running, distributed systems and that's a lot more complex than writing a Java program that makes some things move. So I think robotics is not something that I would advise to high school people. Master's students, graduates, that's another thing. 

Peter Asaro: 

So what should they study? They would want to get a degree in math or computer science? 

Herman Bruyninckx: 

Whatever, but it's an attitude, so you should not come to robotics and say okay, now I have a degree in computer science and I'm going to do more computer science in robotics; or I have a math degree and I want to do more math. No. You have to come with an attitude and say okay, now I've been trained in this, but I have to train myself in a lot of other domains in order to make progress, and that's the right attitude. Be open to learn other domains and the better ones are able to reuse their skills and their models and their way of thinking efficiently also in all domains. So you don't need – if you have a five-year master's in computer science, you shouldn't need five other years to master the domain of mechanical engineer or control. That should take only a year or so. But nevertheless, it's a year. But that's the right attitude: Finding the synergies with other domains because that's where robotics is going to make progress. 

Peter Asaro: 

Is there anything else you wanted to add? 

Herman Bruyninckx: 

Let me see. Probably yes but I don't think of something. One thing I'm always complaining about to the press, that's they're not helping us teachers or educators or researchers in robotics. So the common press, they are stimulating or implicitly putting certain perceptions in the general public's minds about what robots can do. So they always, if they come here to film something, they don't – they are not interested in filming reality. They are interested in filming suggestive things, so that it looks like this stupid robot is intelligently stirring in a cooking pot or something like this. And so they are giving the general public and students the idea that most of the problems have already been solved and there is something like an intelligent robot, but that's not at all the case. In my robotics classes, I'm spending a lot of time in debunking myths and saying to students or letting students understand that no this does not yet work because these are the real problems that have not been solved. It's not because you see something on the movie and that suggests that a certain problem has been solved, that it's also solved. So in the beginning of my first lecture, I show a couple of videos and then I ask students what do you think is inside this robot. And always students think there's a lot more inside than what there's really inside. And then later on when we study the things that are inside, and they say, "Oh, we never realized that this is so complex," because most of the things that robots do are so obvious for humans that we don't think about that. That takes a long time to realize okay, what can we solve, what is the complexity of the things that people think are simple, while the things that people think are difficult are a million solved problems. So most of my students think that it's a tremendously difficult problem to make a robot walk without falling. That's not such a big thing – making the robot and so on. It is with the control algorithm to – not to fall. That's simple. That's the kind of things that people have very wrong impression about. And I hope the press sooner or later is going to change their attitude and help us instead of making our job more difficult. 

Peter Asaro: 

Anything else? 

Herman Bruyninckx: 

No, I think not. That's fine. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Herman_Bruyninckx&oldid=182349 "
