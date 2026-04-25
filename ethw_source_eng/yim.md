1 Mark Yim 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Humanoid Robots 4.3 Modular Robotics 4.4 UPenn 4.5 Funding 4.6 Influences and Collaborations 4.7 Startups 4.8 Flying Robots 4.9 GRASP Lab 4.10 Challenges of Robotics 4.11 Patents 4.12 Xerox PARC 4.13 Advice to Young People 

## Mark Yim

Mark Yim was born in Cheverly, Maryland. He obtained a B.S. in Engineering Mechanics from Johns Hopkins University in 1987 and attended Stanford University where he completed a M.S. and Ph.D. in Mechanical Engineering in 1989 and 1994, respectively. After graduating from Stanford, he joined a startup company (Virtual Technologies) before moving to Xerox PARC , where he obtained a DARPA grant to continue his work in modular reconfigurable robots. He left industry for academia, coming to the University of Pennsylvania for his current position as the Gabel Family Associate Professor of Mechanical Engineering. He is also involved with the General Robotics, Automation, Sensing and Perception (GRASP) Lab. His research interests focus on robotics, mechanical systems and design, modular reconfigurable robots and locomotion (Polybot), MEMS and batch fabrication techniques, and brute force digital time optimal control. 

In this interview, Yim discusses his career and contributions, focusing on his work with modular robotics. Commenting on the applications and the challenges of robotics and patenting, he outlines various collaborations and involvement in robotics projects, including the development of a robotic arm and DARPA's Nano Air Vehicle. Additionally he provides advice for young people interested in the field. 

## About the Interview

MARK YIM: An Interview Conducted by Peter Asaro, IEEE History Center, 15 September 2014. 

Interview #717 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Mark Yim, an oral history conducted in 2014 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Mark Yim 
INTERVIEWER: Peter Asaro 
DATE: 15 September 2014 
PLACE: Chicago, IL 

### Early Life and Education

Peter Asaro: 

We usually just start by asking where you were born and where you grew up and went to school. 

Mark Yim: 

So I was born in Cheverly, Maryland, and I went to school. My undergraduate was at Johns Hopkins University in Baltimore, and I got my Ph.D. at Stanford University. 

Peter Asaro: 

And what did you study as an undergraduate? 

Mark Yim: 

I studied technically it’s called engineering mechanics because at Hopkins at the time mechanical engineering wasn’t accredited yet, but it was basically mechanical engineering. 

Peter Asaro: 

And then for your Ph.D.? 

Mark Yim: 

For my Ph.D. I got my Ph.D. was in mechanical engineering. It was a little bit odd. The way I characterized it is that my degree was in mechanical engineering, my advisor was in computer science, and most of the work I did – well, not most, but a big chunk of what I did was more on the electrical engineering side. I guess that’s typical for robotics. You have to be kind of interdisciplinary. 

Peter Asaro: 

And at what point did you decide that you were going to do robotics? 

Mark Yim: 

When I was in high school I had to write an essay for this class I was taking. I can barely remember the essay, but it was something about you know, it would be really cool to make robots that are scary robots. 

Peter Asaro: 

<laughs>And what was the first robot that you built? 

Mark Yim: 

Okay, so that’s a hard question. It’s hard to say what’s the first robot I built because you have to define what a robot is. So in my mind I would almost think that the first robot that most people today would call it a robot I guess would be when I was in graduate school we built a little Thomas toy car with sensors that drove around and tried to avoid obstacles. 

Peter Asaro: 

When was that roughly that you were building that? 

Mark Yim: 

Let’s see. That must’ve been 1992, something like that, maybe 1990. 

Peter Asaro: 

So you said it sort of depends on how you define a robot. So how do you define a robot? 

Mark Yim: 

Well, so my definition has changed. Lately I say anything that has actuators, sensors and computations, but by that definition a VCR is a robot and your washing machine is a robot. Your car is a robot, so in some sense they are. There are like lots of programmable machines that are robots out there. 

Peter Asaro: 

Did you used to have a more restrictive definition? 

Mark Yim: 

Not explicit but I wouldn’t have called a washing machine a robot earlier. 

Peter Asaro: 

What motivated this change? 

Mark Yim: I don’t know. Once I decided that, okay, I’m getting into robotics and people started talking about, well, what is a robot? And it’s hard to say, especially the thing that I get frustrated with is when people think about humanoid robots and thinking that’s the ultimate robot thing, and that’s my latest thing that bothers me is that we need to have when you build and design a robot to do a task you want to approach it without any preconceptions of what that thing should be, the shape of it, and people often think it should be like a person because they’re a person, and a lot of times that’s not the right shape for a given task. 

### Humanoid Robots

Peter Asaro: 

Have you worked on any humanoid robots in your career? 

Mark Yim: 

I made a couple, so a couple different ones. One of the things I do is what’s called modular robots. So that just means essentially you make these robot components that you can put together into different ways, and we have put them together into little humanoid robots that kind of walk around. They’re not very good humanoid robots, but they can have the shape and two arms, two legs and they walk around. And also I’ve helped other people on the DARPA DRC project a little bit as well. 

<break in recording> 

Peter Asaro: 

– project? 

Mark Yim: 

My Ph.D. was designing and building a modular self-reconfigurable robot, although we never actually got to the self-reconfigurable part. We simulated it and came up with planning techniques for that but in different types of locomotion, but mostly it was designing and building this modular robot. 

### Modular Robotics

Peter Asaro: 

And what got you interested in modular robots? 

Mark Yim: 

So it’s kind of a funny story. I was doing my Ph.D. with Jean-Claude Latombe who at the time was quite famous for path planning and motion planning, and I was looking for a thesis topic and so I was at that time doing sensor-based motion planning. And while trying to think about topics Marc Raibert had built this kind of a hopping robot, which was pretty popular and I was thinking, wow, that’s pretty interesting. And I decided, well, what other types of locomotion are there that’s out there for robots? And I said, well, no one’s built a cartwheeling robot, mainly just brainstorming different types of topics. And then I said, well, how would I built a cartwheeling robot? Well, it would have multiple legs and then from a design point of view you would want each leg to be the same so you wouldn’t have to design a bunch of different – you’d only have to design one leg and then repeat it. Then I thought, well, you could also make each joint the same so you’d only have to design one joint. And then you might have a bunch of them but they’d all be the same. It’d be easier to build, easier to design. And then I started thinking, well, if they’re all the same they don’t have to be in a cartwheel shape. So then I told my wife, I said, “I have an idea. You know, I think maybe I could build this robot that’s made up of these modules and you can reconfigure them,” and then she said, “Well, why would you have to reconfigure them? Have the robot reconfigure itself.” “Well, great idea,” so <laughs> I started making this self-configurable modular robot. 

Peter Asaro: 

And what are the biggest challenges for modular robots and self-reconfiguration? 

Mark Yim: 

There are a lot of challenges. At the beginning I think the biggest challenge was and probably still is the computation side. How do you program them? The interesting thing is when you have lots of them, when you have hundreds of thousands of millions of modules that can form all these different shapes, but coming up with algorithms so that all those thousands or millions or whatever can work together to do some task is hard. So there are a lot of people who also, especially in computer science, found that interesting, and they’ve been approaching that problem. So I think we’re starting to make progress on that. I think on the mechanical side one of the things is if you have lots of modules you want to ideally put – if there are lots of them and they’re all small they’re all weak, and so you’d like to be able to put them together in parallel so that you can get things stronger by making them bigger and that type of thing, and that’s not clear how to do exactly, just building a nice mechanism for that to happen so that everything can work together in an additive way. Right now we build modules. We put them together. If we put them in parallel they often fight and it’s hard to make them work together. So there’s that side of things, technical aspects. 

There’s a community now, which is nice. There’s dozens of researching groups that are doing modular self-reconfigurable robots. About 10 years ago we got together and we had a meeting with a bunch of them and we said, “What are the hard problems? What are the hardest problems?” And at the time we said, “We can do all these things. We can- we’ve shown that we can do all these things. The hardest thing now is finding the killer app. What do we do with it?” I think that’s still a problem. We don’t know what to do with it. The idea is that you have these building blocks so you can theoretically do anything, but you can't do anything well, to some extent, and certainly not better than a device specifically made to do that one task. There’s another interesting story. In talks I would say, “Why would you want to have a modular reconfigurable robot? There are these three promises. It can be uh..versatile because you can change its shape to whatever it needs to do. It can be uhm..low cost because if you have a lot of repeated modules you can use batch fabrication techniques and- and, you know, make lots of them cheaper. It can be robust because it can self-reconfigure. If some of these extra modules are bad you just throw them away and then reconfigure and you’re- you’re fine.” After I did that like five years later we had another conference and the guy said, “You know, the three promises, but the problem is right now they’re all super expensive, they break all the time and they can't do anything useful.” So, yeah, there are promises but we’re not there yet, and I think we’re still not quite there yet. We’re still trying to figure out, well, how can we actually make them useful, and that’s the thing I’m thinking short term now is we’ve been doing this for 20 years. Is there something where we can actually do something useful with them? 

Peter Asaro: 

So what do you think are some of the promising application demands for that kind of technology? 

Mark Yim: 

Well, the clear one is applications in which you don’t know what you need to do, so you need to be able to reconfigure and adapt to the environment, so space exploration, any type of exploration thing where there’s a big unknown then we have an advantage there because the adaptation ability is much greater than you could do with a fixed configuration shape. Other ones are highly constrained environments. So, again, space exploration. You can only send up a certain amount of volume and mass. It’s very expensive to send it up, so instead of sending 10 different robots that have 10 different functions then you could have one robot that can do those 10, maybe not as well as those 10 separate would. They could still do those 10, just a lot more efficient, so that’s the type of thing that I think would work. Search and rescue is another one that I still think is possible where you can – you know, confined spaces, robots can get through confined spaces and then reconfigure into whatever it needs to reconfigure into. The problem is that both of those applications are really narrow, you know, not a big market, that type of thing. So I’m hoping to find something that has a little bit larger impact. 

Peter Asaro: 

And you built some snake robots that have a modular form? 

Mark Yim: 

Yeah, so it turns out the snake form is great for a lot of things, for especially going through obstacles in cluttered environments. I don’t know if I can tell this story. 

Peter Asaro: 

That’s all right. 

Mark Yim: 

So I was on a family trip going down the highway once visiting relatives in New Jersey, and on the way home in the car my kids in the back were playing or whatever, and then my youngest son started screaming, “Snake! Snake!” And I thought they were just playing, but there was actually a snake in the car. So we pulled over and the kids got out, and I saw this snake. It was about two feet long, right on the seam of the backseat. And then when I tried to get it, it climbed up the seat and then into a small hole about that wide and then disappeared into the back of the car. So we took everything out of the trunk. We banged around. We couldn’t find it. After 10 minutes we thought maybe it was gone, so we started putting everything back. The kids got back in. It popped out of a different hole in the back seat and then I was able to grab it and throw it away. But the shocking thing for me was that it was this tiny hole that it could get into and then maneuver itself in the structure behind the chair. That type of maneuverability was – if you could have a robot that could do that in a cluttered environment it could be really very powerful, so that was kind of the inspiration towards doing a little bit more on the snake robot research. 

### UPenn

Peter Asaro: 

Great. And how did you get from Stanford to UPenn? 

Mark Yim: 

Okay, that’s a bit of a story, too. Right after I graduated from Stanford I went to a startup that a friend of mine had already done. This was building virtual reality glove devices, so I worked on haptic feedback for this glove device. 

Peter Asaro: 

What was the name of the company? 

Mark Yim: 

It was called Virtual Technologies. And then at the time I was still thinking a little bit about my thesis work where we’d build modules that were maybe two or three inches on the side, roughly. And everyone always thinks it would be really interesting if you could make them really tiny, shrink down the mechanisms and then you could have lots of them. That’s when you could go to thousands or millions or something like that. And so MEMS technologies at that time was just growing, so microelectromechanical systems, and I saw an advertisement at Xerox PARC where they were looking for someone to do research in that area, so I moved from the startup to Xerox PARC. And then I learned a little bit more about the MEMS and things like that, and then there was DARPA – actually, I was approached while there by a program manager. Actually, it was one of the office directors of DARPA, and he wanted me to be a program manager. And I was relatively young at the time, and so before I was thinking it’s probably not a good idea to do that too young, so I didn’t do that. And that program was in the direction of what my thesis work was in, so they made the call and then instead of running the program I decided to apply for the grant from them instead, and so I got a grant and that was pretty nice. It ended up being like $4-1/2 million. So I was able to push the modular reconfigurable work further while at PARC. And then after that work then an opportunity came to come to Penn as a professor. A lot of people sometimes say that’s unusual to go from industry to academia. I know it does happen but maybe not as much as the other direction. So people often ask me why did I do that, and there are multiple reasons. I was always curious about teaching. I did some teaching while I was at Xerox PARC, as a lecturer at Stanford, which is fun, but also a bunch of things were happening that I didn’t like at Xerox. They had some layoffs. I became a manager at the time and having to do layoffs was really very unpleasant, so I decided I didn’t want to do that anymore. And then there were family reasons also. My family was on the east coast, all that kind of stuff. So then I came to Penn, and that was about 10 years ago. 

Peter Asaro: 

What are some of the other differences between doing this kind of research in an academic setting that’s at a university versus a research setting in an industry? 

Mark Yim: 

Okay, that’s a really good question. The industrial research very often is focused on the company, so you want to be able to contribute to the bottom line of a company and that’s important. Xerox PARC at the time was also kind of a special place. A lot of people did some very interesting things, and essentially you had to make a story about the research that you were doing and how it ultimately could affect the company’s business. And I got pretty good at doing that. In fact, the modular reconfigurable robots is one thing that we said that, you know, you could make a modular printer. Xerox is just making marks on paper. And it ended up actually that Xerox did make a kind of modular printer to some extent where there were multiple things, and it was actually – I think it’s still a product now. But one of the problems is there were a couple of ideas I thought were really cool like flying. I wanted to look at flying robots. And I could make the story about flying robots and somehow the control is similar to controlling paper and all that kind of stuff, but in my heart I knew, okay, the link is not that great, but I can make a story to sell it to do the research but I felt guilty. I felt guilty that I was doing this research that I didn’t really believe would hit the bottom line for Xerox very well. So moving to academia and moving to Penn enabled me to do what I call guilt-free research. Sorry about that. Yeah, so guilt-free research I think is – and you can do anything, which is the nice thing about academia. Of course, you have to get funding to some extent, but you’re much freer than you can in industry. 

### Funding

Peter Asaro: 

So besides DARPA what were some other funding sources that you’ve had over the years or grants? 

Mark Yim: 

So lately it’s much more from NSF. I’ve been involved in several large projects with the army as well. I had some funding from Willow Garage, which is kind of a robot research company. 

Peter Asaro: 

What was your relationship with Willow Garage? 

Mark Yim: 

So I was on their board of advisors. Very early I helped them hire some of the first people. Every summer I would go there pretty much for five or six years, so I’d do a variety of research for them as well as do some advice on the management side and that kind of thing. The CEO I met while I was at PARC, and he’s a good friend of mine now. 

Peter Asaro: 

We’ve interviewed him for the series as well. 

<laughter> 

### Influences and Collaborations

Peter Asaro: 

So who are some other people that you’ve collaborated with over the years? 

Mark Yim: 

So Vijay Kumar, we’ve done a lot. He’s the one actually who first got me to come to Penn, and he’s really great. I’ve also done stuff with Daniela Rus, so she and I, our research areas are very similar. We had several big projects. Daniela typically leads these projects but with a lot of other people in this modular reconfigurable robot community. Hod Lipson and Eric Klavins were in that group as well. Lately I’ve done a lot with an architect. There’s this architect at Penn called Simon Kim. So I guess the past five years – has it maybe been five years – we’ve been doing kind of electromechanical art. So he’s a little bit kind of on the art side, so it’s like robotic performance art. So we’ve done a ballet. We did Shakespeare. Actually, we’re pretty excited. This semester I’m doing a class with Simon where we’re working with opera. We made some contacts at Opera Philadelphia, and one of their composers is working with us to develop this. We’re really excited. We have no idea what it’s going to be like, but we’re going to do a performance at the end of the semester, and it should be interesting. 

Peter Asaro: 

Very interesting. And so could you also talk a bit about some of your teachers and advisors and people who sort of mentored you or influenced your work? 

Mark Yim: 

Okay, so my advisor was Jean-Claude Latombe in computer science, and so he was interesting. One of the things I really appreciated was that he funded me but at the same time he gave me lots of freedom to do the research that was not necessarily in his area. Like all of the mechanical design and building stuff was not what he usually did, but he appreciated it, which was really good. Another person that I really credit a lot for being where I am now is Ed Carryer. He’s a professor at Stanford as well. He taught this class. It was called Smart Product Design Lab. It was essentially mechatronics, what people now call mechatronic systems. That was kind of the eye opener for me after I took that class. It was like now I know that I can build things and I know how to build things, and I suddenly felt enabled in terms of, okay, I can build a robot. So that’s actually what also got me interested in teaching because that was so impactful for me I wanted to be able to do that for others, so I did a little bit of that at Penn as well. 

Peter Asaro: 

And what did you build for that class? 

Mark Yim: 

That’s where the first robot, the car that drove around, that was from that class. It wasn’t a very good robot, <laughs> but it was still, you know, it kind of worked. 

Peter Asaro: 

It was a robot. 

Mark Yim: 

Yeah. 

Peter Asaro: 

Great. And any of your Ph.D. students who are working now in robotics? 

Mark Yim: 

So I think I’ve got maybe five students who have graduated by this time, and they are all in industry and doing different aspects of electromechanical design. Some of them are, well, according to my definition of a robot, definitely robots. They’re not like humanoid robots. One of them did work on flying quadrotor-type systems, but several of them are in startups. One was at MIT Lincoln Labs, although I think he might be moving. Another one is at Harvard, the Wyss Institute. So they’re all still in that area. 

### Startups

Peter Asaro: 

And have you ever considered doing a startup yourself? 

Mark Yim: 

Yes, in fact, I have just done that. A couple weeks ago Penn has been trying to encourage professors to do startups, and they have a special process called UPstart, which is an infrastructure to allow professors to do a startup while avoiding all the conflicts of interest while being at a university. So that’s really exciting. I think actually making some near-term impact with a company should be really exciting. 

Peter Asaro: 

So can you tell us about the company or is it all secret? 

Mark Yim: 

<laughs>So it’s not secret. It’s all built around some IPs that we’ve recently filed. There’s basically an arm, a low-cost arm that can extend out, and then it turns out you can do it in a way that the structure can be strong and you can have strong actuators, relatively slow but still really strong, and make the whole system really cheap. So the low cost is the thing that I think is the one thing that may be its biggest advantage. Normally if you look at a robot arm I think roughly the cost of the arm goes by the square of the radius of its reach. In our system we expect it to be linear, so it’s for especially large reach areas it can be much cheaper than a normal robot arm. And so right now we’re thinking about things like fruit picking as a possible application, but there could be any type of – what I’m hoping is that it’ll be an enabler for the things that people talk about of your home robot, you know, Rosie the Maid or whatever that goes around. So we’ve done a little bit of studies with Willow Garage, actually, initially. We’re looking at designing mobile manipulators for indoor environments. And in that case the majority of the cost is in the arm or the arms. So if you have a low-cost arm I think you can now start to have low-cost mobile manipulators in the home. 

Peter Asaro: 

And are you looking at making it modular in the sense that you could attach it to different kinds of platforms or different kinds of robot bodies? 

Mark Yim: 

Possibly, yeah, yeah. I also have an NSF grant on exploring robots in nursing homes, so we’re going to put that arm that we’ve developed onto a mobile base that might go into a nursing home and do some of the ADL, activities of daily living, for elders that they need help with that as well as maybe monitor healthcare, giving them water or whatever they may need, that type of thing. 

Peter Asaro: 

Great. And so are you working with any of your students on that project? 

Mark Yim: 

Yeah. 

Peter Asaro: 

So what was the process of creating this startup? 

Mark Yim: 

Oh, the startup, sorry. So some of the students are involved. I mean it wasn’t founded – none of them are founders. Essentially – I forgot. You know, we had this idea. I submitted an invention disclosure and we filed a patent, and then I heard about this UPstart program and I said, oh, well, sounds good. Let’s try it. <laughs> and so it all started from there. And of course students are involved in helping to develop the research around that particular product. 

### Flying Robots

Peter Asaro: 

Great. So you said you also did some work on flying robots? 

Mark Yim: 

Yeah. So there are so many stories. I don’t know if – 

Peter Asaro: 

The stories are the best part. 

Mark Yim: 

Okay. So I had a collaboration with Vijay Kumar a long time ago. It was this what was called Nano Air Vehicle for DARPA. So actually we were subcontracted through Lockheed. Lockheed had this idea for this maple seed flyer, a thing that spun around like a maple seed, a single wing. It was a really cool idea. And Vijay and I, our part was to do a control for that system, and we did that. And I don’t know what happened, but all of my interactions so far with Lockheed have been bad. This one we finished our part and actually a little bit early, to some extent. I mean we came up with a simulator. We showed them all the stuff and I think it was working pretty well. There were other parts of the program, which were struggling with how to get the propulsion and all this other stuff, so they cut us out. They said, “Okay, well, we have to give your money to the other guys,” because we did our part well. You know, I guess you take a hit for the team <laughs> is the only way to look at it. But I wasn’t too happy about that. But at the same time that was my first foray into – well, not my first, but it turns out I had another patent on a different type of flying mechanism. But combining what we were looking at for that with this previous patent, which I had while I was at PARC, we started looking at flying devices that can do attitude control but in a cheap way. So, again, low cost and efficient. So I had this one student who came up with this idea. Normally in a quadrotor you’ve got four rotors and that’s how you can get thrust and moments and all that kind of stuff to do attitude control. On a helicopter you have this swashplate. You’ve got one blade but there’s this kind of linkage mechanism of a bunch of motors that will cause as the blade swings around to pitch, and that’s how you can get the thing to have different moments. And a student had an idea of let’s get rid of all these linkages, instead just have a hinge that’s loose that’s on an angle. It’s a weird angle. So as the blade goes around if you pulse the motor you can get that angle to change just by its inertia. So essentially you get rid of all the linkages. You only have the motor that you’re driving with, but instead of just driving the motor you pulse the motor in different ways you can get these moments to occur. So it’s now much simpler, much easier to make, easier to maintain and lower cost. But you can get all this with the functionality that you need. So that’s one thing that’s happening. 

I have another student who was looking at paths of stability. So like in quadrotors one of the main things you have is this inertial measurement system to do the control because it’s not stable. If you don’t actively control it it’ll fall over. So he’s come up with a passive stability mechanism, and he studied all the dynamics. If you add these what we called dragplates. If you add structure that so when it’s moving in certain ways it’ll be passively stable. You don’t actually have to actively control it. You can just turn the motors on and it won't fall over right away, so that’s kind of interesting. Again, it’s kind of like making things lower cost. You don’t have to put all these expensive sensors on there. 

There’s another funny story, if it’s okay. I was at a conference a while ago. Maybe it was 10 years ago. It might be more. Well, it was probably more than 10 years ago – where people were just looking at flying devices. And there were three talks on helicopters. The first talk was Peter Corke , and it was just beginning. He said, “Here’s our helicopter, our autonomous helicopter. We can't get it to do anything. It doesn't fly,” something like that. “It’s a hard problem.” And then the next person came on and this was a guy from Berkeley and said, “Here. Here’s our autonomous helicopter. We can get it to fly and, in fact, watch. We can get it to land.” The third guy comes on and it’s a guy from MIT. He goes, “Here’s our autonomous helicopters. We can get it to do acrobatics.” <makes flying sound> Flying around like crazy <laughs> and we’re going – at the end we said, “What’s going on here? We got three people. You know, Peter is an excellent researcher. Why do we have these three obvious different levels of performance?” And the conclusion was the sensors. The <inaudible> gyros on the acrobatics one, was a really nice, really expensive one. Peter was trying to get by with these really cheap ones, and it’s very difficult. So building on that – of course, things have gotten cheaper now, so a lot of people can do it cheaply, but at the same time if you can get rid of the sensor you can make things a little bit more robust and lower cost. 

### GRASP Lab

Peter Asaro: 

Well, they’ve been doing a lot with flying robots at the GRASP Lab. 

Mark Yim: 

Yes. 

Peter Asaro: 

What’s it been like working at the GRASP Lab? I don’t know if you can tell me about that. 

Mark Yim: 

So the GRASP Lab is really great. The GRASP Lab is really great because of the culture. There’s enough critical mass. There’s over a dozen professors and over 100 grad students, maybe 200 if you include undergrads and everyone else that’s involved, so there’s a lot of people that are all focused on robotics, and they’re all high quality in the different aspects required for robotics, mechanical, electrical, computer science. And there’s a culture of collaboration. That’s really nice. So we’ll do a lot of different projects together, and you can always go to another guy who’s an expert in their field and, “Well, what do you think about this,” and do things together. So I think that’s really special. I think there are a couple of other places. I think CMU also has that type of thing, but there are a lot of places that don’t, so I think the GRASP Lab is really great in that sense. 

### Challenges of Robotics

Peter Asaro: 

So what do you see as the biggest challenges for robotics or your areas of robotics going forward? 

Mark Yim: 

So in my area, this modular self-reconfigurable robot area, I think the biggest near-term challenge that I would like to see addressed is making something useful and relevant. There are certainly difficult interesting problems further down the line, but I would like to see something useful near term. <laugh> One of the things I think is kind of the big nut to crack a little bit further down the road is what I call task specification. So if you have a robot if we think of a modular robot that can have all these different shapes how do you know what shape it needs to be in in order to perform a certain task? To do that you have to know what the task is and understand the task in a way that you can formalize it so that you can then address that as a problem. So breaking down a task into how a robot could do that task I think is kind of an interesting – if you look at it in the most general sense it’s applying forces on different locations, and that’s super general. Like how do you encode physics in general and then get something to apply to those forces, and that’s really hard. 

### Patents

Peter Asaro: 

So you mentioned a number of patents. How many patents do you have, and what are some other interesting patents that you’ve developed? 

Mark Yim: 

I think I’ve got 40. Well, if you include international it might be like 60 patents. I lost count. So there are a couple of patents while I was at Virtual Technologies that became very valuable, so Virtual Technologies was acquired by Immersion, another company, and then they sued Microsoft and Sony, so these patents had to do with vibration feedback for – in this case the lawsuit was over gaming devices. 

Peter Asaro: 

The rumble – 

Mark Yim: 

Right, right, the rumble controller for the PS2 and the Xbox. And so Immersion won the lawsuit and it ended up being $108 million or something like that. So that was an interesting process, <laughs> just the whole process of going through the lawsuit and all that kind of stuff. But another interesting thing about the process for me, just to throw out another story, I had to do a deposition. You know, as the normal law process you go and you do a deposition. And I had to go to this law firm of Sony, the opposing people, and on the table there was this booklet. They were just showing off, like here’s the west coast lawyer’s magazine or something like that, and it said, “The best lawyers are currently in the west coast,” and they had this list, you know, the top 10 or whatever, and they had circled their name, and they were number two. And the number one was our lawyers. 

<laughter> 

Mark Yim: 

I randomly ran into an elementary school classmate of mine who was a lawyer, a patent lawyer, and he said, “I heard about this case, and I’m gonna go watch because these are like the giants. The- the two patent lawyer giants are gonna battle it out,” and so they just want to come and watch. It was like that big of a deal, at least among the patent lawyers, which is kind of funny. 

Peter Asaro: 

And it really came down to the patent in the case? 

Mark Yim: 

So the whole law process and all that suing process is, I don’t know, it’s a little bit funny because you have to get the jury, and what you say to the jury and how you say it is important and all this kind of stuff and what exactly the truth – they make it really funny. So, yeah, ultimately ideally if the process is good then it comes down to whatever you write and whose ideas are right, but a lot of times – I don’t know. I was a little bit jaded after going through that process. 

Peter Asaro: 

But you still see the value of patenting your work. 

Mark Yim: 

Oh, you have to, yeah. And if you want to get value for the company you have to do that. The lawsuits actually going to trial is rare. Most of the time the value and the patents come from negotiations and that type of stuff. 

Peter Asaro: 

And even when you’re working for academia you’re still producing patents and turning them into startups? 

Mark Yim: 

Yeah, much less than when I was in industry but, yeah, it’s happening a little bit. 

### Xerox PARC

Peter Asaro: 

And so what was it like working at Xerox PARC and what other kinds of robotics were going on while you were there? 

Mark Yim: 

So at PARC when I was there, there was no other robotics. I started a group there and got five or six people to come on, and we had a little robotics group. I think after I left there were still others that were doing that. Again, it depends on your definition of robots. We were the only ones who call the stuff we did robots. My current definition everyone was doing robotics. <laughs> So PARC was really interesting, too, because you have, again, this building full of world’s experts in physics and lasers and software and human anthropology and just studying the way people work, you know, the whole variety of people, which is really interesting. And that’s kind of what made it special, too, not that there was a really strong thing in robotics but that we had a really interesting variety. 

Peter Asaro: 

And were you collaborating with these other disciplines and people while you were there? 

Mark Yim: 

A little bit, yeah. We had several projects with some of the physicists at one end of the building. We talked to the anthropologists sometimes, but we didn’t end up making anything along those lines, but it was interesting always talking to them. 

Peter Asaro: 

Was Lucy Suchman still there when you were there? 

Mark Yim: 

She was. I think her group changed and she wasn’t there shortly before I left but, yeah. How did you know Lucy? 

Peter Asaro: 

She’s a good friend of mine. 

Mark Yim: 

Oh, really? 

Peter Asaro: 

<laughs> Yeah. Okay, so is there anything else that we’ve missed that you want to talk about? 

Mark Yim: 

I don’t think so. 

Peter Asaro: 

Any other fascinating patents? 

<laughter> 

Mark Yim: 

No, I can't think of anything. 

### Advice to Young People

Peter Asaro: 

Okay, so the question we usually wind up with is what’s your advice to young people who are interested in a career in robotics? 

Mark Yim: 

So what I usually do with young students – well, not even young students, but what I do with my undergrads, especially advisees, I tell them to think about where you might want to be five years from now or maybe ten years from now and don’t think about how you might get there, but think about like a dream. So for me when I was in grad school and I said, well, five years from now a dream would be to be in a place where someone gave me millions of dollars to build robots that I wanted to build. And of course it came true with the DARPA contract. The thing that I tell them is think about this dream. Don’t think about how you might get there, but as you go along, as time goes on and you come up with choices think about if you have this choice and that choice and one of those choices closes the door or makes it impossible for your dream to occur just don’t choose that one. Choose the one that leaves it still possible for that dream. And if you keep going along sometimes you end up there, and that seemed to have worked for me so far a couple times. 

Peter Asaro: 

Great. Well, thank you. 

Mark Yim: 

Sure. This was fun. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Mark_Yim&oldid=203600 "
