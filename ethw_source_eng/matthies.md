1 About Larry Matthies 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Work with Computer Vision 4.3 Beginning Career in Robotics 4.4 The Mars Rover Program 4.5 Insight on Career with NASA 4.6 Thoughts on Robotics Field 

## About Larry Matthies

Larry Matthies received his PhD in Computer Science from Carnegie Mellon University in 1989, then moved to the Jet Propulsion Laboratory, where he is a Senior Research Scientist. He supervised the Computer Vision Group for 21 years and has been coordinating internal technology investments in the Mars office for 2 years. His research interests include 3-D perception, state estimation, terrain classification, and dynamic scene analysis for autonomous navigation of unmanned vehicles on Earth and in space. He has been a principal investigator in many programs involving robot vision funded by NASA, Army, Navy, DARPA, and commercial sponsors. He initiated new technology development that impacted every U.S. Mars surface mission since 1997, including visual navigation algorithms for rovers, map matching algorithms for precision landers, and autonomous navigation hardware and software architectures for rotorcraft. He is a member of the editorial boards of the Autonomous Robots journal and the Journal of Field Robotics, and has been an Adjunct Professor of Computer Science at the University of Southern California and a lecturer in computer vision at Caltech. He is a Fellow of the IEEE and was a joint winner in 2008 of the IEEE’s Robotics and Automation Award for his contributions to robotic space exploration. 

In this oral history, Larry Matthies covers his professional life in the field of Computer Robotics, taking us through his collegiate education and his career in robotics research, specifically his work with computer vision. Matthies offers his personal insight on the various projects he has collaborated on as well, from working for DARPA to NASA and his experience with the NASA Mars Rover project, for which he dedicated most of his career to. Matthies also touches upon his move back to academia and his thoughts on the future of the field of computer robotics. 

## About the Interview

LARRY MATTHIES: An Interview Conducted by Peter Asaro with Selma Šabanović, IEEE History Center, 3 June 2011 

Interview #802 for Indiana University and the IEEE History Center, The Institute of Electrical and Electronics Engineers, Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Šabanović, [email]. 

It is recommended that this oral history be cited as follows: 

Larry Matthies, an oral history conducted in 2011 by Peter Asaro with Selma Šabanović, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

Interviewee: Larry Matthies 

Interviewer: Peter Asaro with Selma Šabanović 

Place: Pasadena, CA 

Date: 3 June 2011 

### Early Life and Education

Larry Matthies: 

I was born in Saskatchewan, in the town of North Battleford in Canada. I was the oldest of five boys, so I did my education up through bachelor's degree in Saskatchewan. Then I went to the University of Waterloo for a master's in computer science and then Carnegie Mellon for a Ph.D. in computer science. 

Q: 

And how did you get interested in computer science? 

Larry Matthies: 

Actually, when I was in grade twelve, I took the grade eleven level computer science class and up until that time I was interested in chemistry. I just enjoyed programming, I found it a fun challenge, decided to try that in the university and never looked back. 

Q: 

Who did you work with at Carnegie Mellon? 

Larry Matthies: 

I started with Hans Moravec but he was not in the computer science department per se, he was in the robotics institute. So I needed to have a computer science professor as a co-advisor which was Takeo Kanade and then along the way I switched from Hans Moravec to Steve Schaffer but I was still with Takeo as a co-advisor. In fact, Takeo was really my main mentor all the way through. 

Q: 

What was your first sort of project as a graduate student? 

Larry Matthies: 

I was working in Hans Moravec's mobile robot lab on stereovision for autonomous navigation of ground robots. There was a problem of trying to estimate the motion of the robot as it drove through the environment by using the imagery to track features in the scene, so I made improvements to that algorithm. At the time I did not actually believe that that was the most important thing to be doing but it turned out thirty years later that that it is now called visual odometry and it is actually very valuable and very widely used and many people have worked on the problem since. 

### Work with Computer Vision

Q: 

How did you get interested in vision? 

Larry Matthies: 

Actually as an undergrad, I got interested in artificial intelligence and then for my master's degree I ended up studying computer graphics. I still wanted to do artificial intelligence and I thought the best places to do that were the big schools in the US that were doing that, so that is how I ended up at Carnegie Mellon. In my first year at CMU, I got a little disillusioned with artificial intelligence but computer vision still had some of the same appeal but it had also some of the appeal that I had found in computer graphics. So I tried that and in particular, Hans was working on computer vision for robots, so that was exciting and I enjoyed 
it. So that appealed to me because it had some of the same visual gratification you get from computer graphics but it had a strong theoretical foundation which I was looking for as well. 

Q: 

What disillusioned you about AI? 

Larry Matthies: 

Pardon me? 

Q: 

What about AI disillusioned you? 

Larry Matthies: 

Well, at the time, I do not want to be unfair to the field, but at the time AI was kind of a collection of problems that we did not know how to solve yet and once we knew how to solve them they were no longer considered AI. The very fact that we did not know how to solve them meant we did not have a good theoretical foundation in some cases, at least not a strong mathematical foundation. And at least the particular things I had been looking at, at the time I was not happy with the degree of theoretical basis to them. In computer vision, it is really founded in strongly in physics and mathematics and you know, much of the curriculum you would find in electrical engineering for example. It is pretty cross-disciplinary in that respect but it draws on engineering and applied math disciplines quite a bit. 

Q: 

What year did you get to Carnegie Mellon and what kind of systems were you working with as far as the vision of computers? 

Larry Matthies: 

I got there in the fall of 1981 and I started working on vision in the fall of 1982. When you say what kind of systems? 

Q: 

Like what was the technology like that you were working with? 

Larry Matthies: 

Well, as a robot to do the vision work with, we had something that looked like a little tricycle, about the size of a tricycle. We were working with computers that – I do not remember exactly what we had then but I think the VAX 1170 might have been about the right timeframe. And they did not have a lot of memory so there had been a lot of work, in years just before then in writing vision software packages that could swap images in and out of memory so that you could actually process something in reasonable amounts of time. So things were a lot slower. There were central mainframes. The PDP10 that the department had, I do not think we did much of the research on that but you know, everybody had terminals. We did not have our own desktop computer in those days. The kinds of cameras that we used, this was before solid state cameras really. I think Vitacom's, basically a much lower quality imaging device than we have now. I work on vision for robotics, so it is a multisensory problem so you are combining the vision sensors with inertial sensors. In those days, inertial sensors were big and heavy and very expensive. You basically did not use anything but the cameras. That is kind of a quick overview I guess. 

Q: 

Where did you go then after Carnegie Mellon? 

Larry Matthies: 

After Carnegie Mellon, I came here in 1989, and I have been here ever since. I did a lot of interviews when I graduated, twelve or fourteen, including universities, federal labs and companies and what I was enjoying at CMU was robotics for outdoor applications. I was looking for a place to do that and this was basically the best opportunity to do that. I was not necessarily interested in space per se, but once you get here, it is nice to have a ringside seat on the space program and it is certainly exciting to work on space applications. It so happened that I dropped into a perfect niche for me. The research I had been doing was exactly what was needed for Mars rovers at the time and it has gone to Mars since, so it is really panned out well in that respect. 

### Beginning Career in Robotics

Q: 

I am curious, since you mentioned you were in field robotics, at the time at CMU did they have a field robotics lab or what kinds of labs do they have, in particular, the ones you worked in? 

Larry Matthies: 

I was in the computer science department. I think the robotics institute was founded a year or two before I got there, in 1979 or 1980. There were some smaller labs so Hans Moravec was running the mobile robot lab. This was before the field robotics center, before the term field robotics had been popularized and Red Whittaker who started the Field Robotics Center and I think there is two institutions there but anyway, he was still a professor of civil engineering and I think while I was there was when the Three Mile Island incident happened and that was a big thing that propelled him along in robotics and the DARPA Autonomous Land Vehicle Program happened while I was there and I think Red was involved in building up testbed vehicles for that. Basically Red grew in mobile robotics while I was there and I think FRC got set up while I was there, toward the end of my time there or maybe just after, I cannot remember now. 

Q: 

And is that when the term started to become popular? 

Larry Matthies: 

It probably started then. I think it grew probably through the 1990’s, as you know, Red and others were addressing field-type applications in space, military and mining and agriculture. 

Q: 

What were the big challenges for field robotics as opposed to just mobile robotics? 

Larry Matthies: 

Well, there is basically a contrast of people working indoors on level floors where there are only two types of terrain. There is smooth level floor and then there is discrete obstacles. You can represent the world in two dimensions and do all the path planning in two dimensions. Weather is always good, the lighting is always good, whereas in field applications, you have got uneven terrain, you have got ground cover, you have got different soil types that some of them are drivable, some of them are not. You have got a variety of lighting conditions, you have got a variety of weather conditions, you have got dust that can foul the sensors or you cannot see through. You have to represent the world at least in 2.5D if not in 3D. You have to make inferences about physical properties of the world that you don't have to bother with indoors... it is a more complex problem. It is more expensive to work in that domain. You know, typically, you need a bigger robot, you need just a lot more logistics and infrastructure to do field applications. So, it is not studied as much or fewer places have the wherewithal to do that. 

Q: 

And how did those play out in your first projects at JPL? 

Larry Matthies: 

When I got here, NASA and JPL were working on a program called Mars 
Rover Sample Return. So the acronym was MRSR, the vision was to do a sample return from 
Mars; They had a fair bit of money. Actually, CMU and JPL were funded under that program so JPL was working on wheeled robots with stereovision. We had quite a big robot that was... I am not exactly sure of the size but it was probably fifteen to twenty feet long and to the top of its camera mast it was probably ten feet high. And Carnegie Mellon was working on alternatives, basically a legged vehicle using laser range finders. So we had quite a bit of money and a big team to do field work and the field work that we did was... there is a dry river wash next to JPL called Arroyo Seco so we would load up the vehicle on the trailer and go out there and do test runs. I do not know what the budgets were but that takes a lot of financing to run that kind of experiment. Compared to working indoors, you buy a little robot two-feet in diameter and you know, work with one or two grad students and that is all you need. So, very much a difference in scale between what you could do in a university or at least most universities and what you could do at a federal lab, or you know one or two companies like Martin Marietta that were working on that at the time. 

Q: 

What were the challenges of the vision system for the sample return mission? 

Larry Matthies: 

The algorithms were very slow. You have to have 3D perception since that is how you could determine where the terrain was smooth enough to drive and where the obstacles were and so we were working on that with stereovision and [inaudible] was working on that with laser range finders. The stereo algorithms were very slow so one of my first big breakthroughs was designing a new stereovision algorithm that had much better computational complexity and basically reduce the runtime from half an hour per image to six seconds per image. That was a huge breakthrough at the time and feasibility of outdoor robot navigation. 

Q: 

Did you work a lot with CMU still at the time or? 

Larry Matthies: 

Not directly. We were funded by the same sponsor, working on the same kind of mission but we were working independently. Since then I have had collaborations, in the twenty years I have been here, had collaborations with CMU people a number of times but when I first got here, it was not directly collaborative. 

Q: 

What were some of the later collaborations? 

Larry Matthies: 

I may not get these in the right order, or at least chronological order, but CMU managed to get funded by NASA to set up an organization they called at the time, the NASA Robotics Engineering Consortium. It is now called the National Robotics Engineering Consortium and so that was a vehicle to try to channel NASA-funded research into commercial applications and there was a mechanism where while you could propose joint projects, between say us, CMU, and the company that would try to take a piece of NASA technology and spin it into personalization. So, I worked with Sanjiv Singh on a few things on that and then along the way, the Army Research Lab funded a program called the Robotics Collaborative Technology Alliance and I have collaborated a little bit with Martial Hebert along the way on that. Al Kelly was a grad student. DARPA had a program called Demo II. Us and CMU were part of the Demo II program working on different parts of the problem and we collaborated a little bit there and I hired Al Kelly for one or two summers as a student to bring his path planning capabilities and merge it with our vision capabilities here. And after that, I don't remember if it was still Martin Marietta then or Lockheed Martin, but it was taken to Denver to put on the robots for Demo II. We worked with Tony Stentz who does a lot of path planning work as well. I am probably forgetting people, but those for me personally have been the most direct and the most substantial collaborations. 

Q: 

We heard a little bit of history about the sample return sort of getting cancelled and then evolving into the other Mars builders. Were you working on those and were any of those systems that you worked on supportive to that? 

Larry Matthies: 

Well, the Mars Rover Sample Return program, I was working on when I first got here and I do not remember exactly when that got cancelled, but it was fairly shortly after I got here, within the first two or three years. It was simply unaffordable. Then the pendulum swung to the other extreme of looking at micro robots and that was far less capable but also far cheaper. And we managed to sell this mission called Mars Pathfinder, which was the first lander that NASA-JPL did with airbags and every mission has to have some science, but it was as much a technology test and demonstration mission as it was a science mission and the same was true with the rover. The rover was a technology test and demonstration. It had to have some science. It was fairly minimal science and it was cheap. I think it was twenty-five million dollars just to do the rover. So, I was involved in that a little bit. I did not work directly as part of the mission team but it had a sensor called a Light Striper for detecting obstacles that was having some performance problems. And just coincidentally in parallel, I was working on a next generation Light Striper and I got involved in essentially debugging what was wrong with the one that was headed for Mars and there turned out to be a problem with the optical design that I was able to isolate and then we got an optical engineer to come in and redesign it. 

Q: 

Could you tell us a little bit about what a micro robot is like compared to the previous idea? 

Larry Matthies: 

Well, it is behind me, I suppose we do not want to turn the camera. The Mars pathfinder rover which was named Sojourner, weighed about 11 kilograms. I am not sure if that is the exact number. The Rovers that had been looked at for Mars Rover Sample Return were probably, close to a ton. I do not know the exact number, but we are talking two orders of magnitude, different in weight and whereas the Sojourner rover never went more than six or eight or ten meters from the lander. The original concept for the sample return rover was to go hundreds of kilometers and be a self-contained mission, whereas Sojourner was dependent on the lander and the cameras on the lander and the communication system on the lander to be told what to do and to communicate with Earth. But nevertheless, that mission did firmly convince the whole Mars science community of the importance of mobility. Essentially, the vision of how to explore Mars was never the same after pathfinder because now everybody realized you have got to have mobility because there can be stuff just out of reach from the lander, that is where the big discoveries are and what we found in the Mars exploration rover mission which those two rovers have covered an order of twenty kilometers in seven years. You know, we are several kilometers away from where they landed and that is where the big discoveries happened. I guess I am straying from the original question but you know, the difference between the micro rovers at ten or eleven kilograms and staying with inside of the lander versus sample return -- well, the Mars science lab mission that we are working on now, the next rover, I think it weighs nine hundred kilograms and it is supposed to drive an order of twenty kilometers... that is the difference. 

### The Mars Rover Program

Q: 

And were you involved on the Mars Explorer Program? 

Larry Matthies: 

The Mars Exploration Rovers? Yes, my whole career, I have been in research, so I have never worked on the flight software or been formally part of the mission team, but key elements of the capabilities in that mission came from either me personally or my group. Those rovers use stereovision to detect obstacles, that basically is the outcome of work I did in my first year here. They use visual odometry to help keep track of where they are and more importantly to detect right when they are slipping. That basically grew out of my Ph.D. thesis research. The path planning software that is on there, I did not have any personal hand in developing but that was done by somebody in my group and I basically convinced him that he should as a career move, get involved in the mission. Later on, there were some things that were added after they already landed as kind of the mission software uploads. There is software on board that does basic image processing to detect when a dust devil goes by. That software was developed by somebody in my group. That mission, halfway through developing the spacecraft, like two years before launch, they realized that they had underestimated what the wind velocities might be and there was a concern that the horizontal velocity of the lander might be so large that the airbags might rip on impact. Some people came to us and it turned out that there were retrorockets on board that could be used to reduce the horizontal velocity if you knew what that velocity was. Then the problem became can we get a velocity sensor. And the traditional way to do that is with a Doppler radar but there was not time or money to put that into the mission at that point but coincidentally, they had designed in a camera that they were not using and the question was could they put that camera back in and aim it down. It was originally designed to be on the rover looking up to trap the sun but could we aim it down instead of up. Track features on the surface during the sand and estimate horizontal velocity. We mounted a crash effort, <laughs> pun intended, to try to develop that capability and that was successful. And that was used for both landings and for the sphere of rover, after the fact reconstruction, it may well have saved that mission because it did lead to the retrorockets being fired, kind of reduced the velocity by about a factor of two. So for the MER mission, I also had a hand in helping keep track of where it is, besides, this visual odometry thing that operates kind of over short distances. I work with a photogrammetrist named Ron Lee at Ohio State University on mapping and there is a bundle of adjustment software that Ron's group has developed that is used to keep track of the multi-kilometer traverse and is part of the whole mapping package that Ron's group has developed to generate terrain maps as the rover goes along. I think that is pretty much what I did in that mission. Basically, most of the autonomous navigation capabilities in that mission came out of my group. 

Q: 

What were some of the most important breakthroughs that you feel you have had? 

Larry Matthies: 

Well, real-time stereovision. In the 1980's, the dominant paradigm was to try to do stereovision by matching edges because that was thought to be much faster and when I got here I could see that for off-road navigation in desert-like terrains, using edges was just the wrong way to do it, so you really needed to use what was the alternative paradigm which was area-based cross correlation. Finding an algorithm that was fast enough for real time was something I did and that was a key breakthrough. This whole visual odometry business was something actually I did at CMU before I left there. I think that was not at the time, so I developed the first accurate visual odometry algorithm, even though we were not calling it visual odometry then and that was a good advance over what had been done previously but it was not that important. I think, over the years since then, we have recognized it is a very important capability. Along with some collaborators, some I advised with Takeo and Rick Szeliski, we did a well-known paper that was one of the first to show how to process images in an incremental fashion to build 3D models, much better techniques of course have emerged but that was one of the first to show that you could incrementally build 3D models from image sequences. Well, the thing I just mentioned about vision systems for Mars landers, trying to rule out a velocity estimation during landing, when I got here in the mid 1990’s, I managed to get funding to work on landing hazard detection. Essentially, I built a team that has been working on various approaches to landing hazard detection with imagery and LIDARs. None of that has gone to Mars yet but over the years we have built up quite a bit of capability to be able to do that and I believe someday, will go to Mars. Precision landing has been another important thing, especially for Mars and more or less the same team that I built up here has been working on how do you recognize landmarks during descent, that you can reduce the positional uncertainty from say, plus or minus twenty kilometers, to plus or minus one hundred meters. And that would make, far more of the planet accessible and if we could land one hundred meters from interesting terrain instead of twenty meters from interesting terrain or twenty kilometers from interesting terrain. You know, now you can get there in a day instead of getting there in months. Other things that I have worked on for space application include two explorer asteroids that have a lot of craters. We have developed algorithms that can use the craters to navigate a space craft around asteroids. JPL has been working on balloon missions for Titan which is the big moon of Saturn that has a thick atmosphere. There is a question of, how do you know where the balloon is? We have been working on taking algorithms, the fundamental algorithms that were developed by others and applying them in this domain so that you could take imagery from an ordinary camera on board and register that to radar data taken from an orbiter. That kind of cross registration of different sensor modalities can tell us where the balloon is – that is the NASA side. I have been working on defense robotics for more than twenty years and that grad school most of my work was funded by the defense department. As a funding strategy, I've tried to find things to work on that had relevance to both NASA and other agencies. Off-road navigation fits, so the focus on terrain understanding. Even while I was at grad school, I collaborated with Hans Moravec and Alberto Elfes, they had a fundamental breakthrough in an algorithm called occupancy grids for world model representation and Alberto and I wrote the first paper on combining data from multiple sensors in occupancy grids, that was sonar and stereo. And then with funding from DARPA and the Army Research Lab, I was the first person to use near-infrared imagery for terrain classification of vegetation for off-road navigation. The first person to recognize that you could use LIDAR to classify tall vegetation which can be difficult to discriminate, you can drive through it but it can be difficult to discriminate that from a real obstacle that you have to go around. There is something that we call negative obstacles in this business, basically, any hole in the ground. They are very hard to see. They are still very hard to see. You know, the only good way that has ever been discovered to find those is from the air. But you cannot always send an aircraft ahead of you. Along the way, I discovered that there is just kind of a physical property in the way heat transfer works, that the interior of a negative obstacle tends to keep itself warm. That has not completely solved the problem but it was an interesting advance that makes it somewhat easier to detect those than it would be otherwise. In looking for things that I could work on that other people were not doing, water bodies in off-road navigation that are hazards to navigation. We have myself and collaborators here have put a lot of effort into how do you detect water bodies from a ground robot, we have made a lot of progress towards solving that problem. It does not have wide impact but it is something fairly distinctive that we have done. I think that is a fair selection of highlights. 

Q: 

Has optic flow been a concept that you have used in some of your visual odometry? 

Larry Matthies: 

Certainly I have used it. What we do in visual odometry, tracking features through the image sequence is -- there are many different flavors of optical flow, that is a flavor of optical flow. The collaboration I had with Takeo Kanade and Rick Szeliski was essentially using a flavor of optical flow. In my work on ground robotics, I focused on stereovision for 3D perception and motion estimation, whereas there have been other people in the community that have tried to use a single camera and so the problem with a single camera when you are driving forward is, you do not have depth perception directly in front of you because you have no visual parallax. Optical flow per se, has not been as important part of my work because of that but in the last few years I have started to work on micro air vehicles under funding from the Army. Which have very important applications in military reconnaissance and applications in the civil arena and inspecting bridges and so forth but is also very relevant to things for NASA. If you are trying to explore a comet or an asteroid, or even fly a balloon in the atmosphere of Titan or Venus, there are very different scale of machine. But the vision problems have a lot in common. Or if you want have a micro-inspector like a little ball, a foot or two in diameter, on a human spacecraft like the space station or if in Apollo 13 we had a micro-inspector that could have gone outside and had a look, that has a lot in common with the microware vehicle for earth applications. There, you cannot really fit a stereo system and expect to see very far. Optical flow is quite important in those domains, so we are using it. We have not developed new approaches to optical flow, but we are using it for perception for those kinds of systems. 

Q: 

For these various, near-infrared and LIDAR and vegetation detection, what were the robots that you put these systems on <inaudible> demonstrations <inaudible>? 

Larry Matthies: 

Some of that work was done under the DARPA Demo II program, which was using Humvees that were turned into robots. Then there was the DARPA Tactical Mobile Robotics program which, essentially that was before iRobot became big and successful. They developed a little tract vehicle, which initially was called the Urban Robot and later became the Packbot. That program was the genesis of their Packbot product line and, as you probably know, those are now used in the middle-east for bomb disposal. We put sensors, including the well-known SICK LIDAR single axis scanner as a range finder on a Packbot and used that to classify vegetation. The near-infrared was on the Humvee. The thermal infrared came out of another program called PerceptOR where we were basically using all-terrain vehicles that were outfitted as robots, the quad all-terrain vehicles. General Dynamics Robotic Systems has been a big player in army robotics. They built some custom vehicles that are around three thousand pounds. They call them experimental unmanned vehicles. My work has been integrated on those vehicles, sort of Volkswagen-size vehicles. I think those are the highlights of that. 

### Insight on Career with NASA

Q: 

Can you tell us a little bit about the organization of the groups that you have worked in and how they have changed through time, how different groups interact with each other within NASA, and what it looked like when you got here? 

Larry Matthies: 

Well, I was originally in a robotic vehicles group run by Brian Wilcox. Somewhere along the way, the organization decided it was time to have a vision group and I became the leader of the vision group. When that was first created, actually, there was a small number of us working in vision, which they merged with a slightly larger number of people working on star trackers. Star trackers are used in interplanetary crews to keep track of the orientation of the spacecraft. I really was not interested in star trackers and felt that spending a lot of time on them was going to be detrimental to the stuff that I was interested in. I did not really take care of it very well and eventually management recognized that and moved that off somewhere else and left me with just the vision part. And that grew from, originally a half dozen people to as many as eighteen and then we had the succession of reorganizations and the group would get smaller and then it would get bigger again. Along the way, we recognized that from a strictly, a funding strategy perspective there is actually a lot more money in visual surveillance than there is in robotics, or at least vision for robotics. We thought we should participate in that somewhat. We started to get a toehold in airborne surveillance work. And then there was another reorganization where we formed a separate group that is carrying on that work and I am focusing on vision for autonomous navigation. I have avoided moving further up in management because I did not want to be purely managerial. If the question is, “How has the organization evolved within JPL?”, that is it. Then, just within the last year or year and a half, I felt that it was important to try to get more visibility with top management here and more appreciation by top management of the importance of unmanned systems outside of NASA. Therefore, it should be important to address those applications within JPL. I have taken sort of a day a week level of responsibility to try to provide some strategic coordination of robotics for non-NASA applications across J 

Q: 

You mentioned earlier that with some of these missions, the idea that mobility is important became clear. What has been the status of robotics or of unmanned vehicles within NASA? Has it changed through time? Larry Matthies: 

Well, I think NASA has been interested in surface mobility since the 1960’s with the Lunar Surveyor program. There has always been the interest there but I think it was not until the Mars Pathfinder Mission that it was really appreciated as essential, and also that it was recognized that it was feasible. I think there was a watershed there around 1997. Then with the Mars Exploration Rover Mission, we have shown that it is not only feasible for short-range motion, it is feasible for long-range motion and that it is crucial to find rock outcrops that are many kilometers away from where you landed. But as the ebb and flow of research funding goes, it has been a little bit of a hand to mouth existence because NASA – there have been swings of the pendulum within NASA where for periods of time there is very little research funding, per se. There is very focused money or specific things needed for the next mission. But that is another reason why it is been essential to be having other sponsors at the same time, in order to manage the ebbs and flows of research dollars within NASA. To maintain a steady cadre of people working on these problems so that when the opportunities came back within NASA we were still here and still equip to address them. 

Q: 

How does the funding work exactly? How much of it does the group have to create for itself? 

Larry Matthies: 

Most of the funding that we get, we have to raise ourselves. There is some funding that comes through what is called Focused Technology Programs that is assigned to JPL to solve specific problems for specific missions that will kind of trickle down through management to us. But at the more basic and applied research level, almost all the funding that we get is competitively ordered. In universities there is a concept of a soft money position, which is non-tenure track funded by research contracts. It is very analogous to that. 

Q: 

In a sense, the size of the group also depends on the ability to find that kind of--? 

Larry Matthies: 

To raise money. 

Q: 

Okay. 

Larry Matthies: 

Right. Yes. 

Q: 

How much does the funding shape what you decide to do research on versus how much is driven by your interest? Larry Matthies: 

Well, they go hand-in-hand. You have to be pragmatic and realize that if you have to have a charge number and a contract behind that charge number, you have to work on things that people will fund. But that is a bit of a chicken and egg thing. If you bring an interesting new idea to a sponsor, then sometimes they will apply some funding to it. You need to sort of be working under the radar on things that you believe in even if, the country is not ready to apply funding to them. There are ways to get funding for that at, a small level. JPL has some internal seed funding pots you can apply to. You can collaborate with people elsewhere. There could be different agencies like the National Science Foundation that fund basic research that maybe NASA or the Defense Department are not ready to fund; but if you collaborate with those people, you can kind of get the ball rolling and then move those ideas into other agencies. 

Q: 

Have you had much interaction with companies as well? 

Larry Matthies: 

Yes. The Robotics Collaborate Technology Alliance that the army’s been funding, we have always been part of a team, led by companies, General Dynamics. The DARPA Demo II program was led by Martin Marietta. I do not remember if our money came through then, I think our money came directly from DARPA but we were basically working on a team with Martin Marietta. When we were working with CMU and the NASA Robotics Engineering Consortium we worked a little bit with some companies. Toro was interested in automation for some of their lawnmower products. We have had some of our vision software licensed by small businesses. No small businesses that have made it big yet, but we have had some of our software licensed. I actually collaborated with people here a little bit who pioneered the development of CMOS Imagers. The cameras that are in all the cell phones these days, some of the pioneering work on that technology was done here. I was part of a patent for on-chip block averaging for multi-resolution readout, which was part of the package of patents were licensed. That particular capability has not had much impact in the market yet but you can buy it. We have collaborated with other companies in other DOD funded programs. We are doing work for the navy now where we are a subcontractor to other companies doing unmanned boats for the navy. There are probably others that I am not remembering. iRobot, we collaborated with iRobot in some programs. We are collaborating a little bit with iRobot’s competitor, QinetiQ. In the robotics technology lines these days, QinetiQ’s part of that team. We work for Boston Dynamics on some of the DARPA programs for legged squad support system, basically for legged robots. We provide vision systems for legged robots for Boston Dynamics. 

### Thoughts on Robotics Field

Q: 

What do you see as the big outstanding problems facing field robotics over the next few years? Larry Matthies: 

Well, one of the things that we have been working on, which there has been progress – I do not think it has done but for many years, all of robotics research was done in static environments. The problem was hard enough when nothing else was moving that you did not want to have anything moving in the environment. Because we just did not have the perception capability to understand that yet, or the path planning capability to reason about things moving in the environment. A lot of that was just driven by limitations in computational power. We have been working on the perception and representational and planning capabilities to operate in dynamic environments. For Mars there is still an issue of understanding the difference between hard soil and soft soil. The rovers have gotten stuck in soft soil. And there are problems yet to be solved in detecting that before it happens and making sure we get out of it. Back on earth, in the mainstream computer vision community, there has been a lot of work on object recognition. That is a dominant theme in computer vision these days, that will play into mobile robotics. It has not been as significant yet but it is going to become important. As we get the more basic problems of safe mobility solved then you need to do more purpose of mobility and that means you have got to understand things around you as more than just 3D structures. You have got to understand what they are and what they are for. Even just, going through a door, helps to understand what doors are in a semantic sense not just in a geometric sense. There is a growing trend to work on mobile manipulations, robots with arms. Now you are combining all of the problems that come with manipulation, including object recognition, with the problems of mobility. If you have arms on a mobile base, now you have to reason about the degrees of freedom of the arms and the mobile base. I think that is fairly good. 

Q: 

What do you think is the future of robotics in NASA? 

Larry Matthies: 

In NASA? 

Q: 

Yes. 

Larry Matthies: 

Well, the holy grail for Mars is sample return so rovers would be part of that. Right now for Mars we are limited to terrain that you can go to with a wheeled vehicle. But some of the more interesting science may be in terrain that you cannot access that way. We are looking at robot systems that can rappel down cliffs. NASA would like to enable sample return from comets because comets may be where some of the chemistry arose that gave rise to life. An unmanned spacecraft is not the same as robots that you see, roaming around on earth but they have many of the same requirements for autonomy. Free-flying spacecraft that can operate in close proximity to other objects, whether those objects are planetary bodies, like comets, asteroids, or moons, or other spacecraft, like a micro-inspector. Then long-term for NASA, I believe that there will be value to robots for satellite servicing. This has been a debate, in the commercial world, “Is that really economically viable?”, and just within the last six months, I think, there was announcement that for the first time a big satellite operator has awarded a contract, in this case, to a Canadian company to do satellite servicing. But what is made that economically viable is that this is for communications and Intelsat has many satellites, essentially in geostationary orbits, on the equator. You can go and refuel those with one mission that just kind of drifts along the equator, servicing many in one mission. That becomes an economically viable business model. NASA spent five billion dollars or more on a mission called the James Web Space Telescope, which is going to be on the far side of the moon. It is not designed to be serviceable. I really know very little about the mission but I have to wonder, if we could do robot servicing, could we do a better job of great observatories in space and perhaps make them more affordable because they do not have to be so failsafe upfront. Servicing missions are not cheap but, if you can spend five hundred million dollars on a servicing mission as opposed to throw another one and a half billion dollars in to greater reliability so you do not have to service, maybe it is a good idea. We have seen that with the Hubble. We extended the life of the Hubble many times through servicing missions. 

Q: 

There are, of course, autonomous robots and then there is also a lot of telerobotics at NASA. Have you worked on any of the telerobotics and how do you see those two working together or against each other or whatever you would call it? 

Larry Matthies: 

I have not had much involvement in telerobotics. There was a lot of work on that when I first got here but I chose to work on rovers. I do not see that as competition. It is a matter of an evolution and so you do telerobotics where it is feasible and where autonomy is not yet feasible. You do autonomy where that is the only possible way to do it and, therefore, you have invented a way to do it. You can do telerobotics in Earth orbit or potentially on the moon because basically, what makes telerobotics possible is relatively low communication delays. Where it must be autonomous is where the communication delays are too long, so essentially Mars and anything beyond the moon has to be autonomous. Then there are analogies on earth. The same thing goes. Applications that you would do telerobotically on earth – you could think of surgery as a telerobotic kind of application, where you would not dream of not having a surgeon involved with today’s technology. But, at the same time, you would much rather send the robot in to Fukushima than have to send a person. And it is sort of unfortunate that we are not ready as a society to have robots that could be sent in there to do that job. But I think that is a rare occurrence that disasters like that happen, and therefore even though technically I think it is feasible, the investment had not been made, prior to that incident to have the robots ready to do more. They have certainly taken robots in there but we could do a lot more. The capability exists to do more. It is just not matured to the point it is quite deployable yet. 

Q: 

I noticed that you were also on the editorial board of “Field Robotics,” the journal. 

Larry Matthies: 

The journal of “Field Robotics,” yes. 
Q: “Autonomous Robots.” I was wondering how long you have been on those boards and how you have seen the field change while you were there, or emerge <laughs>. 

Larry Matthies: 

I have been on the editorial board for “Autonomous Robo” – I cannot remember how long I have been on either of those editorial boards. I have been on “Autonomous Robots” longer. I have not been the most active editorial board member <laughs>. For “Autonomous Robots”, I review papers occasionally. For “JFR”, I have been a guest editor for special issues occasionally, particularly in space robotics. So how has the field evolved? Since I can’t remember exactly when I started those roles, I don’t really have a good answer for that. 

Q: 

It can be more broad than just from the journal itself. 

Larry Matthies: 

Well, we have examples of things that have actually been fielded. We have been talking a lot about space. Prior to 1997 there had never been an autonomous planetary rover mission. Since then, we have had substantial missions for that. On earth, things like the Packbot and the Talon from QinetiQ are the first deployed military robotic systems. Since I really have not been that involved in commercial applications I cannot say as much about that side but I think there are applications in agriculture and mining and material movement in shipping ports and things like that where we are seeing autonomous vehicles. We have been seeing a lot of work in the last decade or more. The whole robot road following thing, which got a big start in the Darpa ALD program in the mid to late 1980’s, that has gone from something that was just barely possible in a very big, very expensive research vehicle to something that actually works pretty well and is doable in an automobile now. Now we have cars that can park themselves. This has been driven by advances in sensing and especially by advances in computing and by reducing the cost of those things. A big driver that I believe we are going to see in the future is cell phones. Small cameras for cell phones, which lead to images in cell phones, you need to be able to process those images. Now we are getting very substantial image processing capabilities in cell phones. The next thing that is going to happen is now you have got two cameras in a cell phone so you can do Skype on the cell phone. But there are also things coming out so you can have two cameras facing the same direction to aid with teleconferencing. That has a stereo system that you can use for a robot. Because it is a cell phone it is not only going to have a lot of processing power, it is got to be very low power dissipation. I think we are going to see processes develop for cell phones eventually go into small mobile robots, both on the ground and in microware vehicles. Robots, robotics by itself, is too small a market to drive substantial innovation in sensors and computers. But commercial electronics is a huge market that is driving those and robotics will basically ride that wave in sensors and computers. 

Q: 

Our final question. Generally, if you could give some advice to young people who are interested in robotics what would it be? 

Larry Matthies: 

Get a solid grounding in mathematics but not just that. You need to be hands-on so you need to get a solid grounding in computing and the ability to program. Given the multi-disciplinary nature of the field, it might actually be useful to start with an undergraduate degree in an engineering discipline and then possibly do with some computing options, and then possibly move to a computer science department in grad school. I have talked to students recently who are grooming themselves for grad school who are getting a very diverse background in computer science and controls and elements of electrical engineering. I’m very impressed with, you know, the level of maturity and forward thinking I see in people like that because it is a very diverse field. When you get to grad school you cannot be completely sure in advance which direction your interests are going to go and which direction your opportunities are going to go. If you come in with that breadth of background as an undergrad, not only are you more likely to get accepted to a good place but you are more prepared for whatever opportunities arise. If possible, at the high school level. Through the first program it is good to get hands-on experience with projects at the high school level. If you can manage to attach yourself as an undergrad to the faculty doing research get summer jobs or part-time winter internships – not internships really but work with faculty who are doing research, as an undergrad on whatever they need to do, to get that experience and exposure. But also remember that it is, at least today, it is still a fairly small field. While it is growing, there are more jobs in other fields than there are in robotics. Yes, it is exciting but it is still a small field, although I believe, is going to grow. 

Q: 

Okay. Thank you. 

Larry Matthies: 

You are welcome. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Larry_Matthies&oldid=182933 "
