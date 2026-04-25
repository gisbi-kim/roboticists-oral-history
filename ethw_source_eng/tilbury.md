1 About Dawn Tilbury 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Doctoral Thesis: Developing Planning Algorithms for Nonholonomic Systsms 4.3 Collaboration at Graduate School 4.4 Work at University of Michigan: Involvement with Manufacturing Systems Control 4.5 Challenges in Developing Better Techniques for Manufacturing Systems of Control 4.6 Verification and Adjustments for Logic Control 4.7 Role of Robots in Manufacturing Systems Control Project 4.8 Collaboration & Funding for Manufacturing Systems Control Project 4.9 Perspective on Working with Industry 4.10 Implementation of Anomaly Detection Algorithms 4.11 Robotics Reliability Project 4.12 Collaborations & Funding for the Robotics Reliability Project 4.13 Challenges in Robotics Reliability Project: Uncertainty 4.14 Former Student Collaborators 4.15 Synergy Between Robotics & Controls 4.16 Future Problems to Solve: Controls for Human Robot Interaction 4.17 Issues in Human Interaction Through Different Kinds of Interfaces 4.18 Involvement with Service Institutions 4.19 Women in Robotics 4.20 Robotics Program at University of Michigan 4.21 Inclusion of Women in Different Fields 4.22 For Prospective Robotics Students 4.23 Future of Robotics 4.24 Other Personal Robotics Projects 4.25 Funding for Robotics Projects 4.26 Commercializing Projects 4.27 Students 

## About Dawn Tilbury

Dawn Tilbury was born in Minnesota in 1966. Tilbury studied Electrical Engineering and went to University of California, Berkeley for her graduate school studies. At Berkeley, Tilbury took courses on controls and developed an interest in robotics. For her doctorate thesis, Tilbury worked on developing planning algorithms for nonholomonic systems or wheeled robots that cannot move sideways. After graduating from University of California, Berkeley, Tilbury joined the faculty of University of Michigan, where she was involved with manufacturing systems control. Then Tilbury went back to robotics, and collaborated with US Army Tank Automotive Command, working on issues of reliability and user interface. Currently, Tilbury is interested in control theory and its applications in various domains, such as manufacturing systems, network communication, reliability of ground robotics, and dynamic systems modeling of physiological systems. 

In this interview, Tilbury talks about how she became involved with engineering and robotics, her research interests, challenges in the robotics field, mentoring students, her involvement with various divisions within the IEEE, and efforts in involving more women into the robotics field. In addition, Dr. Tilbury gives advice to students of various levels who are thinking of a career in robotics. 

## About the Interview

Dawn Tilbury: An interview conducted by Selma Šabanović, 22 January 2015 

Interview # 795 for Indiana University and the IEEE History Center, The Institute of Electrical and Electronics Engineers, Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Šabanović, [email]. 

It is recommended that this oral history be cited as follows: 

Dawn Tilbury, an oral history conducted in 2015 by Selma Šabanović, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

Interviewee: Dawn Tilbury 

Interviewer: Selma Šabanović 

DATE: 23 January 2015 

PLACE: College Station, Texas 

### Early Life and Education

Dawn Tilbury: 

So my name is Dawn Tilbury and I was born in Minnesota in 1966. 

Interviewer: 

Can you tell us a little bit about your early years and your education? 

Dawn Tilbury: 

I was from a middleclass family. My father was an engineer, worked at Honeywell in manufacturing engineering. He was an electrical engineer. I went to public schools, then I went to the University of Minnesota, majored in electrical engineering like my dad, and then I went to graduate school at Berkeley, California. That’s where I got interested in robotics. Not sure I knew what robotics was before I went to grad school. 

Interviewer: 

Which department did you go to? 

Dawn Tilbury: 

Electrical engineering. 

Interviewer: 

How did you decide to go into electrical engineering? 

Dawn Tilbury: 

Because that’s what my dad told me I should do, <laughs> and he was really smart about it. He told me I should apply to the engineering school because if I didn’t like it I could use all those math and science credits for something else, but if I did like it then, you know, I could keep going and get a good job at the end. 

Interviewer: 

What did you find there? Did you like it? 

Dawn Tilbury: 

I really liked physics, but I had a great physics teacher, and when I was in high school my favorite subject was French because I had a great French teacher. So I thought I should major in French, but my first year in college physics was much more interesting, but I was going to major in physics, but anyways, I ended up in engineering. 

### Doctoral Thesis: Developing Planning Algorithms for Nonholonomic Systsms

Interviewer: 

What kinds of things did you work on when you went into grad school? 

Dawn Tilbury: 

My first semester I didn’t do any research. I took this course on robotics working with Professor Shankar Sastry and took some other controls courses, but somehow I’m not sure why I got into controls. Anyway, it seemed like a good set of classes to take, and then in my second semester I guess that’s when I started working on research with Shankar Sastry and he was interested in these problems on motion planning for nonholonomic systems or wheeled mobile robots. So that was what everyone was working on and so that’s what I started working on. 

Interviewer: 

What were some of your first projects? 

Dawn Tilbury: 

So we were trying to find a better way to plan paths for like mobile robots in the plane that can’t move sideways because you can’t just plan a path geometrically, you need to consider the kinematics of where the car can go. So people had developed ways to solve this problem, but we were always looking for better ways, and not only just with the car, but if the car had a trailer we were looking for multi-wheeled or like long chains of vehicles, cars, and trailers, I guess just because it was harder. I’m not sure that we were working with any companies or anything, but it was a very mathematical problem and I was interested in solving mathematics. 

Interviewer: 

Is that what you did for you PhD thesis? 

Dawn Tilbury: 

Mm-hm. 

Interviewer: 

What were some of the kind of most important problems that you worked on or solved during that time? 

Dawn Tilbury: 

So I worked on this problem of how to develop the planning algorithm where you could think of parallel park a car that has end trailers attached to and is arbitrarily large, and so you’re given the initial position and you’re given the desired final position and you have to try to find a path between the two that uses only the driving input, the vehicle velocity and the steering wheel of the front wheel. At some point we started looking at what if some fire trucks have steering in the back too. So how would you use that extra steering wheel to give you more maneuverability? So we solved that problem too. 

Interviewer: 

Did you work with particular physical robots at the time? 

Dawn Tilbury: 

No, it was purely-- actually all the results were purely mathematical and then we would simulate them and have these little videos that would play on the UNIX workstations, just little stick figure cars. They were not very realistic, but it would give you the sense of how the cars would move. We made assumptions that you understood exactly where you were in the world, that you knew exactly where the angles of all the trailers and angles of all the wheels, so we didn’t do anything that was more practical in terms of sensing or understanding of the world. It was very, like I said, a very controls mathematical framework of a problem, but I liked math so it was good. 

### Collaboration at Graduate School

Interviewer: 

Did you work with any other people at the time? 

Dawn Tilbury: 

Yeah, so there were a bunch of graduate students in the group. The most senior grad student was Richard Murray at the time and I worked with him in the early days. We wrote at least one paper together if not two, and then there were two other grad students that had started at the same time as me and we worked together in different combinations. One was Greg Walsh and the other is Linda Bushnell. So I worked with them, and it was-- I think those were the people that I ended up writing papers with, but there were a lot of students in the lab that you would, you know, just go in and this was the day before not everyone had a laptop, right, so if you wanted to work on the computer you went into the lab, even if you wanted to check your email you went into the lab. So there was more of a community versus people being more distributed connecting over the computer, you were in the computer lab working together, or at least working in the same space, even if not on the same project. 

Interviewer: 

What was the time period that you were there? 

Dawn Tilbury: 

So I was there from ’89 to ’94. 

### Work at University of Michigan: Involvement with Manufacturing Systems Control

Interviewer: 

What did you do after that? 

Dawn Tilbury: 

Then I went to the University of Michigan to be a professor. So I applied to a bunch of different jobs, academic jobs, and got an offer at University of Michigan in mechanical engineering, and accepted that and have been there ever since, 20 years. 

Interviewer: 

What kind of environment did you find at the University of Michigan? Were there people working on robotics? 

Dawn Tilbury: 

So, yeah, there were people working on robotics. In fact, the reason I went to the University of Michigan was Professor Harris McClamroch from the aerospace engineering department. I met him at a controls conference and he’s the one who suggested that I should apply to Michigan for a faculty position, and that I should apply to mechanical engineering, because I never would have thought to apply to mechanical engineering, but shortly after I got to the University of Michigan they started this big research program on manufacturing systems, and so I became involved in manufacturing systems control working with this larger research center, and we used robots, but I wouldn’t say we were doing research on robots. We were doing research with robots, but more industrial manipulators. 

Interviewer: 

What kinds of research were you doing? 

Dawn Tilbury: 

So I was looking at the system level of the control, not how to control the robot or how to control the machine, but how to control the robot together with the machine and the conveyor and the part tracking from the RFID tag in the data base and all that sort of pushing the parts through the factory in the right order at the right time. So developing better ways-- people knew how to develop that kind of control, but it was very fixed and if they had to make any changes it would almost have to be completely rewritten. So we were trying to develop better techniques for control at that system level. 

### Challenges in Developing Better Techniques for Manufacturing Systems of Control

Interviewer: 

What were some of the main challenges in doing that at the time? 

Dawn Tilbury: 

I think the challenge was that there weren’t really good models of how the manufacturing system operated, not the type of models that would be useful for control. They were models that were useful for planning or production schedules and maintenance schedules. So it was more industrial engineering or optimization type of models, but not models about the timing and interaction between the different signals that would go through the system level or logic controller. So we spent a lot of time developing models. 

### Verification and Adjustments for Logic Control

Interviewer: 

What were some of your different projects around these kinds of topics? 

Dawn Tilbury: 

So we looked at actually several different languages that you might-- mathematical languages that you might use to write this logic control, and then how could you verify that it would be correct before you deployed it or before you had to test it extensively, and of course that verification depended on having the model of the system as well. So we were trying to figure out how you could verify that it was correct as well as how you could change it if you were making part A and you wanted to change the line to make part B, what would be the simpler and easy way to change it, and then verify that it’s going to work correctly for part B. 

### Role of Robots in Manufacturing Systems Control Project

Interviewer: 

What kind of role did robots end up playing? So you were mentioning they weren’t really doing research on robots but kind of with robots. 

Dawn Tilbury: 

They were, at least in the specific examples we looked at, they were either treated as machines, like they were doing processing, like they were welding, or they were treated as a material handling. They were moving parts from one part to another, like a conveyor or a gantry or some other material handling system. So we didn’t treat them so much specifically as robots. They were either material handling devices or processing machines in our framework, so. 

### Collaboration & Funding for Manufacturing Systems Control Project

Interviewer: 

Were there people that you collaborated with in this work? 

Dawn Tilbury: 

Yeah, there were in addition to the graduate students, of course who there were a lot, I worked with Professor Pramod Khargonekar, who was in the electrical engineering department at the University of Michigan and I guess Professor Yoram Koren, who was the director of the center, was a big influence in all the work, and the industry partners. You know, we worked with Ford, and General Motors, and Rockwell Automation, and Siemens, and getting their input on what were the specific needs for these different types of system control. 

Interviewer: 

Were they funding most of the work? 

Dawn Tilbury: 

There was a large grant from the federal government but there was also a matching support from industry. 

### Perspective on Working with Industry

Interviewer: 

How did working with industry impact the work? What was that like? 

Dawn Tilbury: 

I’d say it was the best way to work with industry because most of the money came from the federal government and there was a desire to do fundamental academic research, but because we were working with industry we would have access or be able to understand what were the challenges that they were facing in their plant floor today, but I would see that when we’d go talk to them they would tell us, you know, what are the problems we have today that we need to have solved tomorrow, and so then I had to come back to the university and abstract it a little bit and say like, “Well, what could we develop that could be more fundamental, not specifically fix this problem, but fix this class of problems?” So that was challenging but I think it was also rewarding that you could see that the work that you were doing could have an impact in the future because it was at least addressing problems that were currently happening on the floor. 

### Implementation of Anomaly Detection Algorithms

Interviewer: 

Did you see any of the work end up being applied? 

Dawn Tilbury: 

I think over the course of the center, which ran for 10 or 11 years, they changed some of their processes, but it’s not clear that the specific algorithm that I wrote ended up in their controller, but the structure and the framework was changing. So it was all evolving along the same direction. 

Interviewer: 

What were some of the results or kind of deliverables or things that came out of these projects that you thought were important or that you were proud of? 

Dawn Tilbury: 

So there was one result that was quite nice in this area, and this was so-- maybe I should back up a little bit. So we were working on trying to develop new ways to write their logic control that would be more formal and verifiable, and it became clear after several years of this that they were not going to change the way they did their control, at least not in the horizon that seemed reasonable. Things are pretty entrenched in the automotive industry, and they install a system on the plant floor and it runs for 10 or 15 years. They think in long time scales. So we started thinking of what other things we can do that would be related to this system level control, and so we tried to figure out if we could come up with ways to understand problems that they have with their control without changing it. We could at least help them debug it just by watching what’s happening on the network. So we came up with some anomaly detection algorithms that just basically look at the traffic on the network and point to what’s the sequence of events that happen when something goes wrong. So, data mining I guess you might call it, but it was more model-based than that. 

### Robotics Reliability Project

Interviewer: 

So after that what kinds of things did you work on? 

Dawn Tilbury: 

So I got back into robotics because the U.S. Army Tank Automotive Command, which is in Warren, Michigan, was working to consolidate all of their robotics effort with their ground vehicles effort. So they started working heavily in robots and called basically the University of Michigan and said, “Can you guys help us with some of these research challenges?” and so that’s how I got back into robotics after working more in manufacturing for several years, and they were interested-- so this was probably in the late 2000s’, like 2006, 2007, and so there were a lot of robots deployed in the field and they were having huge reliability problems with these robots, and so since we do a lot of manufacturing in Michigan they thought we could give them advice and do some research on how to improve the reliability of these robots that the soldiers were using in the field. So that’s how I got back into looking at reliability, and the aspects of reliability that we ended up looking at are the user interface, how does the operator control the robot, and energy usage, how can you make better use of the limited battery power that’s available, and temperature control, because the robots if they overheat then the motors will shut down. So we’re trying to look at how can you, and again this comes back to a control problem, how can you control the robot most effectively to minimize these types of failure modes. 

Interviewer: 

So what kinds of robots were you working on? 

Dawn Tilbury: 

So we had PackBot, so iRobot, PackBot. So we had one of those, and then we-- those are pretty expensive and they’re proprietary, so we also had a few small commercially available robots. We used the SuperDroid. I think we had a couple of SuperDroids, and then we built some custom add-ons, like a manipulator arm adding on and, yeah, we had some RC cars we played with too, small, ground robots. 

Interviewer: 

Do you mostly do the work in the lab or do you also work in the field with the robots? 

Dawn Tilbury: 

Mostly in the lab. We built some arenas out of plywood that the robots can drive around, like mazes and things like that for people who have to drive it remotely and can get easily disoriented on where the robot is in the maze. 

### Collaborations & Funding for the Robotics Reliability Project

Interviewer: 

Do you have any collaborators in this particular work? 

Dawn Tilbury: 

Yeah, so I worked with Professor Galip Ulsoy and Professor Anna Stefanopoulou, who are both more controls people, but do some work in robotics. I’m not sure Anna does work in robotics, but anyways, she’s the director of the center that we work with with the Army, and Professor Ella Atkins, I was working with her for some of the energy usage. 

Interviewer: 

Did the Army fund the project? 

Dawn Tilbury: 

Yes. 

Interviewer: 

How was that? How did that work? You had mentioned this kind of being federally funded and being partially connected or interacting with industry how was…? 

Dawn Tilbury: 

So this is funded through a large research center we have at the University of Michigan called the Automotive Research Center, and I’d say automotive at least at the Army in Michigan has expanded to include robotics and all ground vehicles. So we work closely with them. They have a staff of researchers there and we meet with them at least two or three times a semester. So what would that be, like 8 or 10 times a year, and then we also have on every project an industry partner that doesn’t give funding, but participates and helps give direction to the project. So we’ve had good connections with industry in that way to fund some small robotics companies around as well as for the energy project we were looking at using a fuel cell. So we had a partner from the company that makes the fuel cells. 

Interviewer: 

Can you name any of the companies that you worked with? 

Dawn Tilbury: 

Yeah, so we worked with AMI is the fuel cell company. Quantum Signal is a small robotics startup. So they do signal processing, vision processing and robots, and then I can’t remember the name of the other company. It was a very small startup. 

### Challenges in Robotics Reliability Project: Uncertainty

Interviewer: 

What were some of the kind of bigger challenges that you had to deal with in this work? 

Dawn Tilbury: 

I think one of the biggest challenges is trying to figure out what’s the real problem, right, because as-- especially in the military as you’re sending these robots over you’re not exactly sure what kinds of environments they’re going to face or what kinds of missions they’re going to need to help with, and it’s almost like after you figure it out then you bring it back to the university, but they’ve kind of figured that one out, and it would be better if we could see further into the future and know what the real needs are going to be because it seems like they’re always trying to solve the problems they had yesterday, and they’re trying to envision what they’re going to have tomorrow, but I can’t imagine that they know. They might think they know, but-- so I think it’s always trying to-- in all these challenges it’s like-- we can frame this problem and solve it but it’s not always clear that it’s the right-- I shouldn’t say the right problem, the most important problem. There could be other problems that are more important. 

Interviewer: 

How did you deal with those challenges? 

Dawn Tilbury: 

I think mostly you just keep talking to people and get feedback on do they think this is a good direction to go, and even if it’s not the most important maybe it’s still an important problem and you should go ahead and solve it, but a student will learn a lot and we’ll write some papers and he’ll graduate and get a job and all those are good things too, so. 

### Former Student Collaborators

Interviewer: 

Who are some of the students that you’ve worked with that have gone to maybe continue working in robotics or work related to the field? 

Dawn Tilbury: 

So one of the first students that worked in this ground robotics with me, Steve Rosar. He’s now a postdoc at Johns Hopkins still working in robotics in teleoperation. I guess the next student that graduated working with these robotics projects just finished in December and he’s going to go work at Ford, so, not really robotics but controls, so. 

### Synergy Between Robotics & Controls

Interviewer: 

So what would be the kind of most kind of interesting experiences or things that you would want people to know about in terms of your research or the kinds of work that you’ve done in robotics or what you’ve learned from the field and what you’ve provided to the field in a sense? 

Dawn Tilbury: 

That’s a hard question <laughs>. So like I said, I started kind of-- so my background has always been controls and really most of my publication is in controls, although I probably certainly there’s a lot of overlap between robotics and controls, and if I understand the history correctly the Robotics and Automation Society spun out of the Controls System Society at some past date, whenever that was. So my primary affiliation has been the Controls System Society. I’m also a member of Robotics and Automation. So I think I would say that robotics is a great application for control because it brings together I’d say a lot of the key challenges in control in terms of motion and perception and sensing estimation, all the way from the low level, you know, trying to control this motor and get this precision that you need in a robot, all the way up to human interaction and human direction, supervision. So I think robotics is a great application for control and I think it can help push new developments in the control field as well as developments in control can help advance the capabilities of robots. So I think it’s a good synergy. 

### Future Problems to Solve: Controls for Human Robot Interaction

Interviewer: 

So for your own work what do you think are some of the developments that like working with robotics in particular have kind of pushed for you? 

Dawn Tilbury: 

Well, so this parallel parking problem I was quite famous for in the day, but that was a long time ago. The more recent stuff I’ve done in robotics I think since it’s only been a few years, like I said, my first student just graduated a year ago. I think it hasn’t had quite the impact yet, and sometimes you need to wait and see what the impact is going to be, and you don’t always-- you can’t foresee into the future. 

Interviewer: 

If we ask you to foresee <laughs> into the future what would you see as kind of things that are coming up for you in terms of challenges or problems that are motivational for you to keep going? 

Dawn Tilbury: 

So I’m starting to get, and a lot of times these directions come up because I have a student who’s interested to go in this direction, and I’m adventurous enough to say, “Sure, that sounds like a controls problem. Let’s go ahead and try it.” So the most recent student I just picked up in the fall is more interested in how robots interact with humans, and so we found-- we, she, I-- there’s another professor in computer science who studies how people understand emotion, and so we’re trying to see if we can have robots try to understand people’s emotion and use that to help determine how the robot should interact with the people. So that’s going to be a very different kind of project than what I’ve done in the past because it’s just looking at a very different aspect of human interaction. Mostly we’ve been doing human interaction with teleoperation, driving with joysticks and things like that, which is different than interacting through speech and gesture and so we’ll see how it goes, but I think it will be interesting. 

Interviewer: 

Are you thinking of working on a particular task? 

Dawn Tilbury: 

Well, so just to get started I think you need a specific task, and so the student is trying to work-- we’ve encouraged her to try to set up a trial run this semester where the robot will just be an animated face on a screen and we’ll give a tour to the human subject, like in a poster session. So interacting through like a-- you might imagine this would scale to a museum or some other kind of tour, but a very focus interaction. In the future I think it’d be interesting to have robot helpers in the house and things like that, but I think you have to start with something very limited context in order to make progress. So we’ll see how it goes. 

Interviewer: 

Who is the other faculty member? 

Dawn Tilbury: 

Emily Mower Provost, she’s in computer science. 

Interviewer: 

And the student? 

Dawn Tilbury: 

The student is Megan Ritchie. 

### Issues in Human Interaction Through Different Kinds of Interfaces

Interviewer: 

So you mentioned that before you were also working on some aspects of human interaction through different kinds of interfaces. Were there interesting kind of issues that you had to deal with there when you actually had to some kind of control that involved a human as well? 

Dawn Tilbury: 

So Steve Rosar, this first student, ran this experiment where users had to teleoperate this robot that had a manipulator arm on it and they had to pick up these boxes with the manipulator arm, which is pretty hard to do from a joystick. So he also had an option for them to use master-slave where you could physically move the robot to pick up the boxes, and what was interesting from that experiment was that the subjects or the participants who were really good at videogames could do it better with the joystick than with the master-slave, because they would get used to it and figure it out, but the subjects who were quite naïve users had a huge benefit from using the master-slave. A lot of them couldn’t even complete the task with the joystick. So I think that taught us and me that you need to consider not just the task, but the user, because some users will be better adapted to certain interfaces than others, and if they’re already adapted, like they’re good at playing videogames you may not need to go to the expense to build this master-slave, but if they’re novice users, you know, like firemen that might only use it once in a while, it will help them a lot. So I think these are the kind of things that you don’t always think of. You think about the task and trying to do the task the best, but it’s not just the task, it’s the closed-loop performance of the user with the task and the robot that you have at hand. 

Interviewer: 

Are there other situations in which you had hit upon this issue of dealing with different things and users or different tasks that affected your work in the controls area? 

Dawn Tilbury: 

So, not yet, but I’m sure we will. Still new at this human users stuff. 

### Involvement with Service Institutions

Interviewer: 

Could you tell us a little bit about your involvement with IEEE RAS, either in terms of service or organizing things? 

Dawn Tilbury: 

So I’ve been involved in-- I’m trying to think of how long I’ve been involved in IEEE RAS. I’ve been involved in Control Systems Society since I was a student, or I’ve been a member since I was a student. So I’ve been involved in a lot of control conferences and I think that I started getting involved in RAS again through this CASE conference, the Conference on Automation Science and Engineering, because it was where I was publishing some of my work in manufacturing control, and so I’ve been-- I’m trying to think if I’ve been on a committee for them. I’ve been to the conference several times. I’m on the committee for ICRA this year. I’m publications chair, and I’m on the editorial board of TASE. I’m the senior editor. So that’s my involvement in RAS. I think I was on some other committee for them. I can’t remember which one though. So I’ve been involved in the IEEE Control System Society and I’ve also been involved in the ASME Dynamic Systems and Control Division, so spreading my professional society around, but it sort of fits my different interests that I’ve had over the years. 

### Women in Robotics

Interviewer: 

So this year you’re also part of this all-women organizing team. So could you comment a little bit on how you see the position of women in robotics and maybe engineering more generally and just your own experience as a woman? 

Dawn Tilbury: 

Well, I think it’s interesting to be on this all-women organizing committee, but I guess the more interesting thing for me is all the organizing committees I’ve been on before for conference have been non-control side, and they’re much smaller. So this is a huge committee by any standard I’ve been on before. I was general chair of the American Control Conference last year. I had a team of 13. So I don’t know how many there are, but there’s more than 13, probably at least more than twice that, if not three times last time I checked. So I think that’s the bigger difference that I’ve seen versus that it’s all women. I think it’s great for visibility that it’s all women. I think robotics is inherently interesting to women, especially when you start-- all the studies that I’ve seen, because I read a lot of these studies about women in engineering, women are more interested in things that can help people, and so I think if you start to think about industrial manipulators, not so much interesting, but personal care robots, very interesting. So I think you start to see that shift in what robots can do, can create more interest in young girls or young women to go into robotics. I was always interested in the math so I wasn’t-- but you know you’re never-- one person is not the rule for all of women in a field. We have a new robotics program at the University of Michigan, and we have eight students coming in last fall and four of them are women. So I think that’s a great odds to get started. I don’t know if we can keep that percentage up as we go forward, so it was a small class, but I think it does show that there’s a lot of really strong women who are interested in this area. 

### Robotics Program at University of Michigan

Interviewer: 

Were you part of the group that started the robotics program? How did that happen? 

Dawn Tilbury: 

So as I understand it there was some strategic planning at the college in trying to look at what areas the college could be strong in, and robotics was one of them, and so they asked me to put together a report about what the University of Michigan should do in robotics, and I brought together a steering committee of five and we wrote a report to the College of Engineering and said we need a PhD program in robotics that across the college, not in mechanical, or electrical, or computer science, to be in robotics. We need a new building where we can all sit together and not be spread into seven different buildings and our students can sit together and learn from each other, and we need an institute that can coordinate all the research activities in the college. So we got the PhD program started last fall. The building is in the planning stages, might go the regents this semester for approval and we are doing a search for a new director for the Robotics institute. So things are coming along. 

Interviewer: 

How does the coordination—that you’re in these seven colleges, how has the coordination between faculty and students worked so far? 

Dawn Tilbury: 

So for the new students that came in in the fall there were two new courses that all these eight students took, as well as a bunch of other students, right. There’s a lot of students interested in robotics, and then for the faculty coordination we have monthly faculty meetings of all the robotics faculty, and monthly meetings of the steering committee which is the group that wrote the report, and we coordinate over email and we have a website. We decided the last thing we needed was another seminar series, so we do not have a seminar series, but we piggyback on the control seminar series, the mechanical engineering department series, the artificial intelligence seminar series, the rehabilitation robotics seminar series, and so you can understand why we didn’t need another seminar series, <laughs> because a lot of those touch on robotics, right, and robotics faculty would be interested to join the seminars but it means we don’t have a dedicated time slot in a week because we were late coming to the game. So we’d have to take over one of those seminars or it would be a lot of work to start our own, just because everyone’s already so busy. 

Interviewer: 

In terms of actually getting the kind of 50/50 balance of student, male and female students, is that something deliberate in a sense or did it just happen? 

Dawn Tilbury: 

I would say it just happened. We couldn’t advertise this program until it had been approved by the State of Michigan, and so we had to sort of, I’d say, cherrypick the best students who had applied to mechanical, electrical, computer science, aerospace engineering, naval architecture, and I think there were six departments. Anyways, we took the best students that had applied to those that looked like they were interested in robotics and invited them to transfer their application from the discipline to this new program, and so I think that was just the mix that it happened to be that year based on who had applied to these different departments with interest in robotics. So I’ll be curious to see what it looks like next year. We have, I think, 125 applications for the PhD program so we’ll see. I haven’t looked at the demographics. I’m not the graduate program chair. That would be Ella Atkins, <laughs> so. 

### Inclusion of Women in Different Fields

Interviewer: 

In terms of kind of the inclusion of women or women’s place and robotics, do you feel like it’s different in any way from control or other areas in engineering? 

Dawn Tilbury: 

No, I don’t think so <laughs>. It would be hard for me to say it would be different, so. 

### For Prospective Robotics Students

Interviewer: 

One thing we also ask because we’re talking about education is if you were advising kind of students who are young people who want to come into robotics, like your new applicant, about kind of getting into the field, or working in the field, thinking about being part of robotics, what kinds of things would you tell them about? 

Dawn Tilbury: 

Well, I guess if they were in high school I’d encourage them to join first robotics if they had one at their school, and take a lot of math and science. If they’re undergraduates I’d encourage them to either try to get involved in research or join one of these student project teams that are like the Mars Rover or these other-- we have an autonomy team that builds an autonomous submarine, or I don’t know, but I’d try to get it involved in one of those student projects. So I think that’d be good for young people to get involved in these team-based-- because robotics you can’t just sit by yourself in a room and build a robot, right. You need a lot of people. You need all these different capabilities. So it’s good to be able to work in a team. 

Interviewer: 

What about in terms, for example, what they can expect from being in the field, what they should be ready for? 

Dawn Tilbury: 

Well, I think it’s an exciting field. I think it’s going to have a lot of changes in the next many years so I think there will be a lot of opportunities for jobs, or startups, or work at companies, or go work at Google, or who knows, whatever they would want to do I think, start their own company. 

### Future of Robotics

Interviewer: 

Where do you see the field going or where do you see the kind of interesting questions popping up these days in control and robotics? 

Dawn Tilbury: 

Like we talked about before I think there’s a lot of interesting questions and interacting with humans on either just through speech and language or physical interactions with humans, especially if you’re going to have robots helping humans, like helping elderly people living alone, do they need to pick them and out of bed into their wheelchair, I mean that’s a hard problem. So I think there’s that physical interaction. I think there’s a lot of challenges there. I think there’s a lot of unsolved problems still in sensing and control can certain can always be improved. I think a lot of the challenges in control is how do you define the control problem, because I think we have a lot of ideas on if you know the trajectory you’re trying to follow you can find a stabilize and controller, but how do you know what the trajectory is that you’re trying to follow, and how do you define that problem when there’s uncertainty in the environment in terms of how the human is going to interact with the controller. I think those are the hard problems. 

Interviewer: 

Are there particular new approaches that either that you’ve tried or that you see going on that you think are promising in answering those particular questions? 

Dawn Tilbury: 

I would say a particular approaches, I think you’re looking at all the fundamentals that have been built up over the years and then generalizing them to different cases. 

### Other Personal Robotics Projects

Interviewer: 

So are there any things that you would like, I kind of asked all of our general questions, but are there particular things about your work that you want to be part of the record that we haven’t maybe touched on? 

Dawn Tilbury: 

No, I think because my work has started in-- well, control of robotics and then went to controlled manufacturing and now it is coming back to controlled robots, I think we did a good job in covering my robotics aspects of my work. 

### Funding for Robotics Projects

Interviewer: 

You mentioned some of your funding sources, but maybe if you just talk more directly where you’ve gotten funding and had over the years and that sort of thing. 

Dawn Tilbury: 

So I’d say primarily NSF and with some-- so from the Army, from this Automotive Research Center, and a little bit from NIST, and I have a grant currently, or I guess a gift from Rockwell Automation, so from industry, a little bit from industry. 

### Commercializing Projects

Interviewer: 

Have you considered at any point doing a startup? 

Dawn Tilbury: 

No <laughs>. I’ve admired several of my friends who’ve done it, but I haven’t had the burning desire, I guess, to take any of the stuff that I’ve done and commercialize. I’ve tried to convince some of my students that they should, but none of them took me up on it either, so. 

### Students

Interviewer: 

Talk about some of your students that you worked with on the board instead of working actively in the field of robotics now that you’ve graduated over the years. 

Dawn Tilbury: 

So because I didn’t start working on robotics at the University of Michigan until like 2006 or 2007, so there’s the one PhD student who graduated who’s a postdoc at Johns Hopkins, and the next one who graduated in robotics is working at Ford, and those are the two so far in robotics. The other ones were in controls or manufacturing, yeah. 

Interviewer: 

And they are faculty now, some are? 

Dawn Tilbury: 

You know, a lot of them didn’t want to be faculty. I have, I guess, two former students who are faculty. One is in Taiwan, and the other’s at the University of Detroit. 

Interviewer: 

And the others went into industry? 

Dawn Tilbury: 

They all went into industry, mm-hm. It’s what they wanted to do. 

Interviewer: 

It also seems like a promising area for control, so. 

Dawn Tilbury: 

Yeah, so, a lot of them went into like defense suppliers, DOD. A couple of them are working at NIST, so government I guess, industry, government. For a while there was a whole pipeline to Raytheon. You know, one guy goes and then they take the next one, and then so-- but they liked it. Some of them are still there, and then they find other jobs and do other things. I’m still in touch with most of my former PhD students, so. 

Interviewer: 

Thank you. 

Dawn Tilbury: 

You’re welcome. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Dawn_Tilbury&oldid=182928 "
