1 About Illah Nourbakhsh 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Book Store Project 4.3 Fundamental Controversy in AI 4.4 Stanford Robotics Community 4.5 Ph.D. Experiences 4.6 Blue Pumpkin Software 4.7 Carnegie Mellon 4.8 Automated Highway System 4.9 Museum Robots 4.10 Other Robotics Project 4.11 Challenges of Robot Interaction 4.12 NASA Sabbatical 

## About Illah Nourbakhsh

Illah Nourbakhsh was born in Tehran, Iran. He completed his bachelor's, master's, and Ph.D. degrees in Computer Science at Stanford University in 1992, 1994, and 1996, respectively. Joining the staff at Carnegie Mellon in 1997, he currently serves as a Professor of Robotics, the director of the Community Robotics, Education and Technology Empowerment (CREATE) lab, and head of the Robotics Masters Program in CMU's Robotics Institute. From 1997 to 2005, he served as the founder and Chief Scientist of Blue Pumpkin Software, Inc., and in 2004 during a sabbatical from CMU he worked as Robotics group lead at NASA/AMES Research Center. 

Nourbakhsh's research interests in robotics include human-robot interaction and systems and community-based robotics. For his work he has received several awards and honors, including being named Kavli Fellow in 2009 by the Academy of Sciences and being inducted into the Junes Harless West Virginia Hall of Fame in 2013. 

In this interview, Illah Nourbakhsh discusses his work in robotics, focusing on artificial intelligence and planning, and the challenges and future of the field. Describing his involvement in projects, such as the Book Store Project and the automated highway system project, he outlines the state of robotics at Stanford, the start of his company (Blue Pumpkin Software), and his arrival and work at Carnegie Mellon. Additionally he discusses his work on educational projects, such as the Dinosaur Hall, and at NASA, and comments on the potential for robotics in education and space exploration. 

## About the Interview

ILLAH NOURBAKHSH: An Interview Conducted by Peter Asaro with Selma Sabanovic, IEEE History Center, 23 November 2010. 

Interview #740 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Illah Nourbakhsh, an oral history conducted in 2010 by Peter Asaro with Selma Sabanovic, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Illah Nourbakhsh 
INTERVIEWER: Peter Asaro with Selma Sabanovic 
DATE: 23 November 2010 
PLACE: Pittsburgh, PA 

### Early Life and Education

Selma Sabanovic: 

If we could start with where you were born. 

Illah Nourbakhsh: 

Sure. I was born in Tehran, Iran. 

Selma Sabanovic: 

What kinds of schools did you go to? 

Illah Nourbakhsh: 

Well, I was born in Iran, but to parents who were travelling a whole lot back then. So they actually had been educated in England and the U.S., and they went back and forth back and forth. So I went to pre-primary, primary levels of education in Iran, but by the time I was in second or third grade I was in Missouri of all places. So I moved from a metropolitan area in Iran to actually a rural family farm area of about 300 people called Platte City which was near Kansas City. And then I actually traveled in a car back down to a private school called Pembroke Country Day in Kansas City, Missouri, and actually went there all the way through high school. 

Peter Asaro: 

Where did you do your undergrad? 

Illah Nourbakhsh: 

When I finished at Pem Day I went straight to Stanford University, and the reason is it was – of all the schools I applied to the only one that accepted me. So it was not a hard decision to make. And so I went there for undergrad. During my undergrad experience there I did a whole lot of work in solar race cars and solar electric cars and computational molecular biology work – protein folding stuff and then robotics. And then I stuck there for the masters and Ph.D. So, in fact, the only school I ever went to outside of Missouri was Stanford all the way through post-graduate work. 

Peter Asaro: 

You were an EE major or a – 

Illah Nourbakhsh: 

I was a computer science major. I started out as a comparative literature major, and then did plenty of that. And in doing that I got to fall in love with organic chemistry of all things because of the geometric nature of organic chemistry and chirality. And so I got really interested in that, and then I got really interested in evolutionary molecular computation and how we could use evolutionary algorithms to figure out how proteins fold. Which is kind of related to the organic chemistry world, and sort of fell in love with AI from there. The idea that you can use computers to solve problems that are hard for people to solve without computers. And so at that point I assumed I'd become a molecular chemist of some kind using computer technology just as a tool box in my back pocket. But then I met a professor from whom I took a really outstanding class called Agents. That was Michael Genesereth, and then he convinced me to start applying my artificial intelligence work to robots. So then we actually went down the path of him buying a robot for me, and me starting to program it. And that's what ended up causing me to stick around at Stanford in the Computer Science Department and getting my Ph.D. there. 

### Book Store Project

Selma Sabanovic: 

What was the robot? 

Illah Nourbakhsh: 

That's an interesting question. You know back then there weren't very many mobile robots on the market. There was only two companies around back then that sold robots to professors – universities. RWI, which stood for Real World Interfaces, and in fact, the DNA of RWI really ended up becoming iRobot over time – Colin Angle and such. But it was RWI back then, and it was Nomadic Technologies. And I used to visit Nomadic Technologies because they were local. So they were right there in Mountain View in literally a garage. Just like the story you hear about Hewlett Packard and all those sort of start-ups that became huge companies. So, literally, in a garage Jim and John Slater, who were brothers, had started this company where they were hand building robots from essentially scratch using 68-332 boards and 68-11's and such. All Motorola processors and they were hand wire wrapping these things. So you would look at the bottom of the boards and there were thousands of little wires running across them. This is before you could do fabs and send things out for layout. And so I talked to them and then Mike Genesereth. The professor and I visited their garage and finally bought the second robot they ever made. 

So we bought this little robot. It didn't even have a – it was Nomadic Technologies serial number two. That was all you could call it. It was a very short swap robot, and back then we put PowerBooks on it. So we put PowerBook 150's and 170's on it – two Macintosh PowerBooks with a Common Lisp. So all the robot programming I did – in fact, for my Ph.D. was in Common Lisp – nearly all of it. Running on two Macintosh computers on top – on a piece of foam on top of a robot platform, and that was the first robot we bought. Fast forward a few years and we ended up doing a lot of educational robotics at Stanford. And for that purpose we ended up suggesting design changes to them as they went into more of a mass production mode. And together we came up with this idea of the Nomad 150 that Jim and John then built, which is a very nice robot – a very robust robot. We ended up buying, I think, four of those and using them for education at Stanford for many, many years. And then fast forward one final time. When I got to Carnegie Mellon we made a cheaper version of that at Nomadic Technologies that I bought six of for here, and in fact, they're still being used here after 12 years as the Introduction robot training class which is kind of astounding after this many years the hardware works. And those are called Nomad Scouts. And they were simpler, smaller versions that the 150 because it didn't have an independently rotating turret. The whole body of the robot rotates all together. 

Peter Asaro: 

What year was that first robot? 

Illah Nourbakhsh: 

That first robot would be 1991, and our job with that first robot was – we wanted to figure out how we can apply artificial intelligence to the problem of robots interacting with people and moving around in the world. So we did work with that indoors, but the most exciting thing we were trying to do was called the Book Store Project. We wanted that robot in '92 to be able to go to the book store and fetch a book for a professor and bring it back. And so we started this thing call the Book Store Project back at Stanford, and had the robot navigating the quad –that really beautiful arched area – the inner quadrangle of Stanford. And that's a repeating area. It's easy to map. So I was out there for six months with a tape measure. We got 1/10 inch accurate mapping of the quad, and it never occurred to us to go look at architectural drawings. We just measured it all and made it all over again – students. 

Peter Asaro: 

Did you have an interest in robots prior to this? 

Illah Nourbakhsh: 

Certainly, I was of the generation –you know there's a class of people you'll meet that will say what I'm about to say, which is – the honest truth this is how it happened. I went to see Herbie the Love Bug because it had just come out in the theaters. And you go to the theatre in Kansas City, Missouri, and it's sold out because everybody wants to see Herbie the Love Bug. And the next theatre in the same complex is showing this new movie nobody knows anything about called Star Wars. And so there is a generation of people like me who went to see Herbie the Love Bug, failed to get in the door, cried and their parents took them to Star Wars. Because what else were we going to do? Go home and let him cry? And then you come out of Star Wars dazed and confused going, ah, R2D2 – I want that robot. How do I build that robot? So part of my interest began indeed with fiction. The other part of my interest began with this idea that my parents really enabled me to build and take apart anything I wanted at home. So I typically would buy things like a Simon, which is an old game that you press the buttons on, and you could program it. You could put it in program mode where you decide what sequence the buttons turn on it. Well, once I could program it I could connect electric motors to it instead of lights. Program it and then the motors would turn on in succession. So I'd make little, simple robots with the Simon as it's brain, and then I could program it and then watch it move. So that was the way a non-programmer back then who doesn't have access to a TRS80 or something could actually build something that's programmable that moves. And so at the same time fiction inspired me – but taking apart toys and remaking them into robots that also inspired me. I was also part of the generation that had the Timex Sinclair zx81 and the trs-80; so in fact, I had a trs-80. Then I got a Timex Sinclair zx81, and I was writing little basic programs. Of course they weren't connected to physical machines, but they do teach you the idea and the power of programming. So that Timex, which I still have at home, and the trs-80 and physically taking things apart and then movies are probably the three tripods of the stool that made me kind of stand up and go, oh, I can do robotics. Growing up however, everybody around me explained to me that robotics was my hobby not my job – not my profession. And that, in fact, computer science and programming was only a hobby and no more than that, and not worth more than that. So I really was disabused with the notion that this is a job, and it wasn't until late in college that it even occurred to me that I could do computer science rather than comparative literature or organic chemistry or physics as a profession – as something that you can actually make a career out of. 

Selma Sabanovic: 

Why was there such a division of computer science? 

Illah Nourbakhsh: 

Well, part of it has to do with the immigrant community and the dynamics of immigration. You want your children to be very successful, and usually that means that your children should become doctors or lawyers because as an international scope those are the two obviously recognized professions. So everything is a hobby except for those two. And I was not from a household where there were professors in my immediate family. There were in my more distant family, but not in my immediate family. So the idea that you can choose any profession you want, and then go into academia in that particular sub-field that was on the table. You're going to be working a job, and so you're going to have to become a medical doctor or a lawyer. 

Selma Sabanovic: 

So when you started working with the robots. I'm curious, why did you start with this Book Store Project? Was there some other type of application in mind? 

Illah Nourbakhsh: 

The thing that I had started doing with Mike Genesereth that we'd gotten excited about was this idea of planning with incomplete information. What does it mean to have a computer make decisions when the computer doesn't have all the information? And can you make decisions in a way that's really effective even with limited information but really fast? So the first thing we did was come up with ways where we have standard planning systems terminate early and make decisions early. And once we had a way of doing that we wanted to apply it to a problem. So I picked a problem which was Wumpus World. It was a video game, and we used the planner to play Wumpus. In doing that we actually named the program Shallow Thought because this is when Deep Thought was being designed. And Deep Thought was about using a lot of computational power to make decisions, and this was the opposite. It was using some cleverness and algorithms and very shallow conceptualization of the problem at hand to make a quick snap decision. But making many, many snap decisions over time and trying to show that the overall behavior ends up being almost as good as making deep decisions once in a while. So Shallow Thought was this video game thing at first, but we wanted a real problem that has incomplete information. And neither of us got just how hard robotics was. We thought if we buy a robot it could move around no problem. But we did get that once the robots moving around its wheels accumulate error as it spins. And so we did get that there will be this constant rush of incomplete information coming into the robot. It had sonar sensors and that's all back then. No vision cameras nothing like that. So to us robots were simply, at first, a practical application of the planning system. It wasn't until we got deeper and deeper into using the algorithms on the robot that we started realizing, my goodness, robots stink. They don't just – they break all the time. The electronics break. The motors break. Everything goes wrong with it. They're incredibly incomplete information, and then people interact with them funny. You have the robot on the quad moving around, and I guy came up with cowboy boots and started kicking it one time. And then it occurred to us, oh, so there's interaction that we didn't expect. People will come and kick you. This never occurred to us, and our plan wasn't designed to incorporate or digest the conceptualization that people might come and kick me. And so that's when we became more excited about this idea that robots are so complex, and such intricate machines in how they're woven into our world in a social level. But they are themselves a really interesting focus of artificial intelligence research. 

### Fundamental Controversy in AI

Selma Sabanovic: 

So after the Book Store what did that lead to? 

Illah Nourbakhsh: 

So there is a guy named Ben Dugan and I who did the Book Store Project together, and we were equals and worked hard on that. And he ended up going to UDub, and in fact, you should talk to him. He is a fantastic fellow – Benjamin Dugan, D-U-G-A-N. Once Ben Dugan and I had worked on the Book Store Project we had big demos. We had in fact, Jean-Claude Latombe, and Barbara Hayes-Roth and John McCarthy and all these people come see the robot moving around in the quad. Then this was exactly when people started having contests around robotics. In fact, Triple AI had just started a contest series, and so we went to the very first contest. I believe that was the one in San Jose. And from then we started more actively being part of that contest circuit. And at first working on the contests by submitting an entry, and then later I started being one of the judges – designing the contest and running the contest. And that's the only time when I started actually weaving into the robotics community. Up until that time I really wasn't aware of what was happening across the country. I was doing planning research. So I understood the planning problems really well around the country, but not robotics itself. That was a mere application area for me. In fact, that first contest Dave Miller was there, and I don't remember where he was. He was on the East Coast somewhere at that point. But Dave Miller had this fabulous robot called Scarecrow, and he saw this interesting collision right there in that first contest because there were poles with barcodes on them. And the idea was that you were supposed to visit them in a certain order and have a light light up on our robot or something. So we knew that you visited them in the right order, and that you recognize these poles. And there was an entry. I think it was Kurt Konolige from SRI who had a very complex entry, and there was Dave Miller who came in with this circuit based robot that didn't even have any programmable matter in it. It was just a circuit. It had a barcode reader, which was a bunch of bristles – metal bristles, and it was jumping around having a little green light bulb light up as it randomly moved around the space – and it won. And it was this sudden collision between hard core conventional AI – we try and solve the problem by having cognition and planning and thinking and problem solving, and clever engineering; where the engineering demonstrates that, in fact, at the behavioral level we can achieve such good results with very little explicit reasoning or decision making. And that battle, of course, only grew in time as Rob Brooks started publishing papers about the idea of using the world instead of internal representation. And then people shot back and, in fact, that is where I saw the seeds of that debate start. 

Peter Asaro: 

Do you see that debate having been resolved? 

Illah Nourbakhsh: 

Well, that debate will stay unresolved for probably all time. The problem is that, fundamentally, each group is able to point out successes and failures in themselves and in the other group respectively. So people who try and design robots bought them up, and use circuits and use simpler kind of progressive techniques are always able to say, look, it's much, much cheaper and simpler to build robots this way. And people who do high-level cognitive work can always pick problems in which they can make a plan or a decision and make it do really well. And then they can point at that and go, look, for this problem our method rocks. The only partial resolution I've seen is this thing that, in fact, David Kortenkamp really pushed hard in his time, and I think he was a major proponent of it which was the idea of what he called tiered architectures, or 3T. The idea that, in fact, perhaps a robot should have at the same time a low level competence that is fast and reactive and witty to its surroundings, and a higher level of competence running in parallel that's reflective and thoughtful and has a little more AI in planning and reasoning going on. Kortenkamp was probably the first person to really nail that down, and what he did on that really stemmed from something Jim Furby had done earlier. Jim Furby had designed a whole simulation system that many of us used back then, and then Kortenkamp used that simulation system to demonstrate a tiered architecture. 

### Stanford Robotics Community

Selma Sabanovic: 

So at Stanford there were other groups that were also doing robotics. What were your contacts with them? 

Illah Nourbakhsh: 

Because I was a student it was really easy to cross the walls and talk to many groups, but it was always odd for me because the groups didn't talk to each other. And, in fact, I'll describe each group to you in detail, but it was funny because – I even had this big meeting where I tried to get all the group leaders in one room at one time, and it worked. They were all in one room at one time, and then they didn't do that again. But there was a number of groups in robotics, and in some cases even using the same hardware. We had Barbara Hayes-Roth who had robots and she was working on believable robot personality. We had Jean-Claude Latombe who was doing landmark based navigation at that point. He had robots with cameras on them pointing up at the ceiling. And they had special types of barcodes on the ceilings, and they were moving around trying to track those barcodes to tell where the robot was. So we had Jean-Claude Latombe, Barbara Hayes-Roth. We had Kurt Konolige at SRI next door—virtually next door who was doing his own robotics work on navigation, and then we had Mike Genesereth and I, the least robotics of the crowd. We were least robot savvy, but we were deep in the world of planning and reasoning and navigation using planners and making decisions of that nature. 

Selma Sabanovic: 

So why do you think they didn't meet up more often? 

Illah Nourbakhsh: 

Well, there's a fundamental trope you'll find across universities which is that universities love to talk and tout the fact that there is a great collaboration. But by and large, it's easier for university professors to collaborate with people at other universities because in doing so they don't threaten the ascription of credit within their own universities design work. And because it was the incremental nature of decision making around tenure and around promotions, everybody wants to carefully protect the idea that they can gradually further a piece of research every year and show modest gradual increases in research stature over time. So because of that dynamic, socially, people tend to work better with people from Berkeley than from their own university, Stanford. Of course, there's exceptions over time, both with people and for twilights of time, when an epic passes during which people can cooperate with one another for four or five years but these pass. 

Selma Sabanovic: 

So in your own work – when you were doing the Book Store were you a master's student at that point or a Ph.D. student? 

Illah Nourbakhsh: 

I got my master's as part of the Ph.D. program. 

Selma Sabanovic: 

Okay. 

Illah Nourbakhsh: 

The robot was called Dervish . The project was the Book Store Project, and we, in fact, did all that work while I was a Ph.D. student. Except that we started it all about a year and a half before I became a Ph.D. student at all. So I was an undergrad. In fact, I got to graduation, decided okay, I'm done. I'm graduating. I better go find a job. I interviewed at Bell Labs. I decided I'm going to go there, and Mike said, "You're not going. You're going to stay here and get a Ph.D." And I said, "But I can get a job now." And he said, "No, you're staying." And of course, he did a very good thing because then Bell Labs essentially collapsed because of the economic recession. 

### Ph.D. Experiences

Selma Sabanovic: 

So what other projects did you do during your Ph.D.? 

Illah Nourbakhsh: 

During my Ph.D. – at the early part of my Ph.D. I finished up the computational molecular biology stuff I was doing where we were matching DNA sequences. After working on the planner – the Shallow Thoughts style planner and then doing the Durvish robot we entered a number of contests where we had navigation systems on robots. And that became probably a common thing that I would work on. We used assumptive programming and a couple of different navigation contests at Triple AI. Everything that I did was around planning with the information. In fact, that ended up being the title of my thesis. It was really this question of should we make assumptions about the world, and then operate under those assumptions until they're violated? And then if they're violated we change our assumptions. So how do you choose the right assumptions so that they can be violated, and you'll find out? Instead of getting killed before you find out they're violated. And then how do you choose new assumptions that are consistent with all the observations you've seen. That assumptive direction and then what we call property based planning where we didn't think about the states of the world anymore. We thought about broad overarching properties that encumbered many, many states of the world. And so we partitioned the world into sets of possible properties that are true or false. That's the finishing work that I did during the graduate program. I was also juggling back then. I was – absurd as it may sound – getting a pilot's license and then instrument flying license for flying under instrument conditions, and that helicopter pilot's license – rotorcraft license. So I was actually doing planning and execution work on robots, and then going and studying and working on flying. 

Selma Sabanovic: 

Did those two ever get together? 

Illah Nourbakhsh: 

They never quite got together, no. No, in fact, there was actually the third thing. In fact, my time was more or less split in three. I started taking very seriously classical guitar, and in particular some Spanish and South American style guitar. And so that's – in fact, I started all three of those pretty much within the first year of my doctorate program, and I continued all of them up until now. Except that for the last four or five years since I had kids I really haven't flown at all. 

Selma Sabanovic: 

Who were the other important people that you worked with during your Ph.D.? 

Illah Nourbakhsh: 

There was a number of professors that I grew really fond of and really close to. One of them is John McCarthy . I ended up having countless chats with him. I worked on a Lego robot with he and his son, and I just really enjoyed his mentality. I enjoyed having conversations with him about robots and vision. He and I were both of the opinion that computer vision had to get much better before we could really make robots work, and I think I still believe that. So I'm still waiting. But John McCarthy ended up being somebody that I really got close to. I had many conversations also – and had as a supervisor John-Claude Latombe, and I'm thinking of the third person – Carlo Tomasi, who was also one of my co-advisors. Carlo was a vision guy, and we did this odd project where David Andre and I did something with Carlo Tomasi back then. It was fun. It had to do with this concept called depth from defocus – or depth from focus. We took three cameras and put them on one of my robots pointed in the same directions but adjust for the focusing positions to be slightly different – so that each one had a different focal plane. And then by comparing the imagery in the three you could start to categorize how far away and how close things were in the scene. So we literally had three frame grabbers –in fact, no, we had one frame grabber. We synced them and had an RGB. One was R. One was G, and one was B. So we turned them into black and white cameras on the RGB lines of a single frame grabber. But this is really fascinating because you could at light speed –very, very quickly move around in the world, detect obstacles, detect staircases, detect bushes. And we even had demonstrations where we put it out and invited faculty to bring their kids, and give the kids treats and have them try to get the thing to go hit something. And have the kids run around with the robot. That's part of what got me interested in educational robotics because working on this idea of depth from defocus yielded a robot that people could interact with safely. Well, when the robot's safe then you suddenly realize the children playing with it are adapting to the robot. They're finding the lowest common denominator and playing. The adults playing with it are trying to figure out how to make the robot break. They're trying to demonstrate that they're better than the robot, and the robot is incompetent at some level of performance. And the children, in fact, as soon as they discover some way that the robot is incompetent cleverly and quickly learn how to avoid that particular stage of interaction. So it doesn't do that, and so it doesn't act silly. And so it can actually interact within a more sophisticated way. That was fascinating and that really got me interested in this question of educational technology and what does it mean to have children use technology, and how genuine and authentic are they with technology as compared to how adults are. 

### Blue Pumpkin Software

Selma Sabanovic: 

So after Stanford what happened next? 

Illah Nourbakhsh: 

Well, when I was at Stanford doing everything I said I also started a company called Blue Pumpkin Software. Blue Pumpkin was an interesting company because there was a particular regime where my friend Ofra Matan and his friend Doron Aspitz had suggested that planning with incomplete information is really useful, and it was in a particular place called scheduling. And the big challenge is, in particular, any situation where you have a ton of people who need to have some agreed upon schedule together but they have preferences and requirements, and I want to take a holiday, and I want to work three days and be off for five days, etcetera. So you have all these crazy constraints coming into a system. How is this system to take many, many people and come up with a schedule that actually maximizes everybody's happiness? Achieves as many of the goals and desires and preferences that they have, and maybe there's some hard rules too. Like union rules that say you can't work more than 30 hours in the hospital. You have to go sleep after 30 hours of work. So we were really interested in this direction, and before there was even a company there was this problem of scheduling prospective Ph.D. students to meet with new faculty at Stanford. And so in fact, Mike Genesereth and I made an interface that was used for years and years after I left. In fact, I used to fly back to Stanford and run the interface for them. Which was absurd to go back from Carnegie Mellon to do that, and it was still running in Common Lisp so we had to go back and deal with it in Lisp on an old computer. But we had this really nice system where all the faculty would put in the students they want to meet with. All the prospective students coming in for the open house would list the faculty they want to meet with, and then we would find a schedule that maximized the number of meetings that were desired, and that was really fun. And it was really application of the same kind of cleverness in making quick decisions, building a partial schedule, and then undoing some of the decisions that were causing problems and redoing some of them. Kind of like you might with post it notes. Swap things around, trade a couple of people and get a better schedule. So we had quite a nice system for that. The company happened because Ofra Montan who was a Ph.D. student and my office advised by the same person, Mike Genesereth. He and his friend decided let's do this for hospitals. So we made the same system for the call schedule of the radiology department at Stanford University. And in fact, they used that for many years. I think for nearly a decade. So all the radiologists put in their preferences. They have different sub-specialties, you have rules about which subspecialties have to be available how much of the time, what hours of the day and night, and the system comes up with two week schedules – two weeks at a time. So everybody knows what to do. This got so extreme that I think – at one point I think they had new Macintosh's running simulations of old windows systems so they could use our old software on their new computers to do the schedule because that was –everybody depended on that as the schedule. Now, things took a turn for the more commercial when it became apparent that call centers have the same problem. Call centers are these places where hundreds, sometimes thousands, of employees are answering the phone. You know, the airlines, may I help you book your flight today? It's the same thing. They have cigarette breaks. They have everything you can imagine impeding upon their time – infringing upon that. And then on top of that you have skills. You have people who speak Spanish other people who speak English. Some people know Windows. Some people know Macintosh operating system. So you have a huge morass of skills and requirements and preferences, and then you have varying call loads over time. The day before Thanksgiving huge call volumes you need lots of agents, but the day after Christmas very low call volume you need very few agents. And so you want to have just enough agents so people don't have to be on hold too long, but if they're not on hold at all you have too many agents. We want people on hold two minutes let's say, but not 20 minutes because then you'll lose business. So it's this massive optimization scheduling problem. And so the last two years that I was a doctoral student we created software around that for call centers. Started a company, got some angel funding and, in fact, that became quite large. And as I graduated from the doctoral program I was the chief scientist of that company, but then I got the offer from Carnegie Mellon right as I graduated. And again, this is the only offer I got. So just as with graduate school and with undergraduate – in fact, graduate school, Stanford is the only place I got into, and it was the only place I applied. Undergrad only place I got into except Berkeley, and then faculty position only place I got an offer from. So I came to Carnegie Mellon and then flew every week back and forth to Blue Pumpkin in Mountain View for, I think, two and half years. And then eventually we sold the company to a much bigger company, and then I was able to spend more time at Carnegie Mellon. 

### Carnegie Mellon

Selma Sabanovic: 

How did you start at Carnegie Mellon? Who was around? 

Illah Nourbakhsh: 

When I started here that was 1996 – I think January of '97, in fact. I graduated in '96, and we went straight to Smith Hall. And back then the old guard of robotics here was fully enforced. The Ultimated Highway System Project was running. Takeo Kanade was director of robotics. Chuck Thorpe was running the AHS system, and I started immediately working on that project. And Matt Mason was here. He was one of my mentors early on. Mike Erdmann was also an early mentor. And, those were the gangs that I really hung out with. My neighbor next door to me was Andrew Marr, so my office was right next to his, which was great because when we moved to this building I was also neighbors with Andrew until he left for Google. And so, those were the people and I was a young assistant professor in robotics and I was a bit of an experiment. Almost everybody that had been hired, not almost, everybody that was in the Robotics Institute was either research faculty or they were co-appointed across multiple departments because robotics was a department, but it was a relatively young department. They didn't have any tenure track faculty that were solo, that were only exclusively in robotics. It didn't exist yet. So, that was really interesting and they hired me as sort of an experiment because I was entirely robotics. I didn't teach any Computer Science classes. I didn't have any Computer Science responsibilities. I wasn't even a courtesy appointed in any other departments, and yet I was tenure track, which was really unusual. Everybody else there was purely in robotics was research track, and so that was `97. And, of course, over the years we've had more and more faculty enter and the department has really swelled and grown well, and has far more funding even than it had in the early years. 

Selma Sabanovic: 

How many people were there then, those faculty and students, around? 

Illah Nourbakhsh: 

We'd have to ask Suzanne. I don't know. 

Selma Sabanovic: 

Okay. 

Illah Nourbakhsh: 

I don't know, probably no more than two-thirds of what there are now, probably even less than that, especially if you count NRAC, N-R-A-C, I don't think it had even started yet. So, in that sense, we were probably at most half the size we are now. 

### Automated Highway System

Selma Sabanovic: 

So, what kinds of – you mentioned the AHS project as some things that you were working on. 

Illah Nourbakhsh: 

Automated highway system, yes. 

Selma Sabanovic: 

Or AHS. 

Illah Nourbakhsh: 

Right, AHS. 

Selma Sabanovic: 

So, what were some of the issues that you dealt with there and what were some of the other projects that you decided to work on? 

Illah Nourbakhsh: 

AHS was a really straightforward application of the work that I had been doing at Stanford with a student, fantastic fellow now, founder of our company here in the area called Parag Batavia. The interesting question there was could you have cars making good, quick decisions about whether to change lanes or not and what's safe to do if they're autonomous cars by using some simple sensing around them without going through a huge amount of planning. And, in fact, we ended up making something called the universal plan where we actually pre-programmed all the possible plans we would need and were able to select the right plan and execute it very quickly. And, that was exciting because then on simulator we could show dozens of cars and show autonomous cars with very little computational effort making appropriate decisions, changing lanes without being dangerous and that was very early work. That was `97-`98. The first big project that I did at Carnegie Mellon University was this museum project. We had this interesting situation so Sebastian Thrun had just done a robot with the University of Bonn in the museum called RHINO and that had gone really well in a small museum area. And, from the phone call I got basically somebody called me from the Field Robotic Center and said Red Whittaker has this project with the Director of the Museum of Natural History. They want a robot and we tried Reid Simmons and he's too busy, he can't do it. We tried Sebastian and he was too busy, he can't do it. We tried Matt and he can't do a robot either, so you're our fourth choice. Would you be willing to do it? So, I was like oh maybe, let's talk. And, so I met with Red Whitaker and with Jay Apt, who was then Director of Carnegie Museum of Natural History. Their idea was let's make a robot that gives tour of Dinosaur Hall, which is interesting because Dinosaur Hall is full of paleontological specimens that are very old, and I loved theirony, juxtaposition of a new robot giving you tours of paleontological data. So, that was cool. It was an interesting idea. And, it was one of the few examples I've seen that's compelling of a robot doing something useful in the human social sphere because in a physical place like a museum you actually want to take people to the exhibits and show it to them whereas there're many cases where people have mobile robots delivering faxes where you can say well we don't need to deliver faxes, we can email them to you, or robots delivering coffee where we say well you don't need them to deliver coffee, it's better for you to get up and walk and get coffee because take a break from work. But, in a museum it almost makes sense for a robot to provide multimedia exhibits that increase your awareness of the physical exhibits around you in the Dinosaur Hall. So, we took on that project in my lab and got some outstanding students to help with it and that really worked out well for us. It turned out that at nearly the same point in time, in fact, Sebastian did a museum tour guide as well, which was Minerva, which was at the Smithsonian American Museum of Natural History. And, that was neat because suddenly you had the paper here publishing stories about the Museum Director here, the Museum Director of the Smithsonian, the robot here, the robot there, kind of the tale of two robots, "The Tale of Two Cities," the tale of two museums, and so that became interesting. For us, that robot project was about human-robot interaction, so we gamed away all the problems of having robots be robust. We put pink markers in the room, used a vision camera, allowed Jean-Claude Latombe’s laminar based planning system so that the robot couldn't get lost. It's hard to confuse anything with a big pink square on the wall. So, the robot couldn't get lost. It plugged itself in and plugged itself out of the wall, and we really wanted a robot that could run for years and years without help. 
The reason we did the project that way was that Nils Nielsson at Stanford, who was also an advisor to me, had published a paper, talking about what he called, I think the Robot Challenge, and the idea was can you make a robot that, in fact, and I can probably dig this up somewhere in my email, but it came straight from him, can we make a robot – he called it the Robot Factotum paper. He said we need a new grand challenge in robotics. Can we make a robot that runs for a full year with its original programming, without humans making changes to the program that does something in our world? And so, we thought well this is the perfect robot factotum example. It's a constrained space. We can put pink marks on the floor, on the ceiling I mean, excuse me, and indeed we could plug it in and plug it out by itself, so we literally hooked it up with an analog pager system. We all wore pagers for five years. That's five years. Okay, it would page us if it needed help. Then it got to the point where we wouldn't go there unless it paged us. So, it had reached a level of autonomy where it only asked for help and we would help it. We no longer had the situation of going there because it stopped communicating and you can imagine the number of just technical hurdles you have to conquer to have something be that sort of industrially available. We also did surveys of the students and children and adults in the area about dinosaurs to see if the robot caused educational impact in terms of their understanding, learning, or excitement about dinosaurs in general and we got really good results. And so, that taught me two things that huge project, the five year project, one was that, in fact, robots can be made reliable enough to be in the physical social sphere. The second thing was that, and by the way they don't crush things, they don't smash babies or anything and they feel safe enough. The second thing it taught me was that we can quantitatively evaluate the educational impact of the robot and wow if we can quantitatively evaluate them, we can have a feedback mechanism. Now, we can go and try and refine how we make robots to make them as educationally impactful and positive as possible. And so, that's how I got into this whole area of social robotics and the formative and sort of evaluation of a robot in society. 

### Museum Robots

Selma Sabanovic: 

Can you tell us a little bit about the robot itself and how you designed it or where you got it and also exactly what it was doing in the museum? 

Illah Nourbakhsh: 

So, the robot itself was something that we cooked up with pneumatic technologies, my old friends Jim and John Slater and their company. We wanted a robot that was holonomic; there was no sideways because people effortlessly able to go down a hall backwards, forwards, go around people by sidestepping them and so we felt that aesthetically that was important for the motion of the robot to be appropriate to the level of cognition and respect for other people to give it in the museum. So, they built some new robots right then called the XR4000, which were astoundingly cool robots. They were huge. They had 24 sonar ring in the bottom and another 24 on top, 24 IR rings. The entire skin of the robot was touch sensitive so it could tell if somebody was pushing on it. It was an amazing robot and we worked with RedZone Robotics locally to build a shell on top of the robot, a head and torso, if you will. So, that was the robot itself and we delivered one from there. It was something like $35,000, which was a lot of money for a robot back then and it was holonomic and fantastic and they were very helpful. What the robot did was we put a laser disc player in it, so this was before we had digital encodings, outside of laser disc domains. So, we had a local company called Magic Lantern create educational shows about various aspects of paleontology from what do the scientists do to why there's disagreements about how the bones go together to visualizations of how the dinosaurs lived, to what the extinction event theories are for the dinosaurs. So, everything you can imagine was packaged up into 3-1/2 minute presentations on the DVD. And then, we had a computer, we had a DVD player, the computer would trigger the DVD player, I'm sorry the laser disc player. The laser disc player would seek and play on a little television screen inside the robot's head and so people would follow the robot around and then it would take them to exhibits that they don't usually visit, like the Aquatic Marine Mammal Exhibit on the side of the building because people would look at the Tyrannosaurus Rex and go wow and they'd leave the room. The whole idea was take them from that experience of excitement and enthusiasm and pull it over to tell them about marine dinosaurs so that they realize that there's much more in the room to look at than just the big T-Rex bones. And so, we take them aside, show them videos, and then even in the future years, in the out years we had quizzes that would come up. They'd answer some questions and that increased audience engagement tremendously. So, we even ended up with touch screens so people could answer questions on the screen by pushing the screen bars. And, that was the whole idea was giving the tour with multimedia experience from the laser disc player. 

Selma Sabanovic: 

How did you design the initial interaction and did you change it with time? 

Illah Nourbakhsh: 

We changed it usually over time. We made tons of changes. In fact, the whole system was this feedback cycle. So, in a way we failed Nils Nilsson's test because we kept changing the software to make it better. We weren't trying to keep it completely frozen and static. The way we designed it was we came up with an architecture for how we could modulate the voice of the robot and how we could have some affection in the robot and parameterize the affection over time based on the interaction it had. So, it could be happy, sad, tired, excited, so we would change the valance of its affect and that have that impact its voice. Then we designed an architecture for how it could dialogue with people, what could it say, what kind of pauses could it have, what visions could it queue and then we presented all this to the education division of the Museum of Natural History and said you guys are educators, you've trained dozens so now you decide what the script is for the robot. What do you want to choreograph? What do you want it to say when it’s tired and somebody's interested in T-Rex's? What do you want it to say when it's excited? And somebody asks about T-Rex's. So, they created the content, including the formative content of how it behaves, and then with them we went to Magic Lantern and actually cut the videos for the laser disc and then we programmed it all into the robot and then using the education division again we tracked people, did micro – what do you call it – we did microgenetic social studies of the people interacting with each other with the robot, did some ethnographic work, did some quantitative evaluations, and then we'd go back and change it all again. And so, really it was this interesting collaboration where pneumatic technologies made the hardware work. We were just the programming glue in a way, but then you had this whole education division of the Museum of Natural History dedicated to tracking and updating the content as appropriate. 

Selma Sabanovic: 

And, why did it end at five years? 

Illah Nourbakhsh: 

Jay Apt left the Museum and when Jay Apt left the Museum they had raised the capital funding to do a major renovation of Dinosaur Hall, so they closed Dinosaur Hall and took out the robot. And, in the new version of Dinosaur Hall there was no room for that robot and it was dated by then. I mean it was a long time for a research robot to be installed in a museum. 

### Other Robotics Project

Selma Sabanovic: 

So, what was next or what other – did you do some other project at the same time as the... 

Illah Nourbakhsh: 

Oh yes. We did tons of projects. If the tour robot in Dinosaur Hall taught us the potential for education, it also taught us the expense of taking on a really big project like that. So, we started trying to do projects where we engaged with the public with less expensive robots, but in much more massive ways outside of Pittsburgh. And so, we did many projects back then. We started something called the Palm Pilot Robot Kit, which is just a simple recipe online for how to convert a palm pilot, which was all the rage back then, into a robot, into an actual moving robot on your table and that was interesting because we could see – you know this was before "Make: Magazine," but we could right away see that millions of people, and back then that was a lot, are going to our website, downloading the recipe, going to Home Depot and getting parts and making their own Palm Pilot Robot, and to us that was super exciting. It also started to teach us about the idea of licensing because companies would come along and say we know you haven't patented this thing, but we want a relationship with you. Can we build a Palm Pilot Robot Kit for you? And, we'd say sure, go ahead and would you pay us some royalties so we can get research funding and they'd say yes, even though we had no patent, no IP, no protection of any kind in the business sense. And so, we learned that the crowd was excited about the idea of getting their hands dirty with robots. We learned that companies were excited about marketing them for us and we learned we don't have to try and go down patent or protection paths, instead we can just keep things open, open source it and still have relationships with companies that generate funding for us. So, it taught us a huge number of lessons that turned out to be critical. We went on to do CMU Cam, which was a small vision system backed with a processor that made it really easy for artists and hobbyists to put vision on their robot because you could ask it things like just tell me where the orange ball is and it would just tell you where the orange ball is. So, you don't have to be a computer vision researcher to have a camera, just like you don't have to be an acoustics expert to use sonar, so it made it that simple in the semantic level. And again, we licensed that to three or four companies and they started selling thousands of these little cameras without us having to ever bother with patents and copyrights or any of that nonsense. So again, we were able to openly share the design, create company empowerments so that companies could actually sell it to people and create empowerment in people because suddenly they can make different kinds of robots from what they could make before. Then became the recurring theme of the lab as we took on more and more projects where we were essentially in the business of empowering people by innovating some new technology and then designing a way to deploy it out into the world. 

Selma Sabanovic: 

And so, I know you've done a lot of other educational projects and also some other museum projects. Could you tell us a little bit about... 

Illah Nourbakhsh: 

Sure, there's too much to tell you. 

Selma Sabanovic: 

If you would pick ones... 

Illah Nourbakhsh: 

I'll give you some examples. 

Selma Sabanovic: 

...that you think are kind of... 

Illah Nourbakhsh: 

It's hard to pick, I mean it's really hard, but I'll give you some examples. The Museum of Natural History had the entomological specimen collection of terrariums with bugs in them and they were bothered by the fact that kids would pass by these terraria and not pay much attention to the bugs. They would just walk right by. And so, they asked us is there something we can do with technology that changes the relationship, the underlying relationship between the visitor in the Museum and the Madagascar hissing roach and the scorpion and the snake and the tarantula. So, we came up with this idea of a robotic terrarium and we called it Insect Telepresence. This is before telepresence was the rage and the idea that we had was well telepresence is going to take off and people are going to be logging into a robot to go to a meeting, but what if you could log into a robot to change your scale. What if by being in a robot you were able to interact with a bug at its scale level. So, in other words, could a robot make you feel like you're the same size as a bug or that a bug is the same size as you? And, if that was the case could you interact as a peer with a bug. And, if you interact with a bug, like with a peer relationship, would that change the degree to which you paid attention to it microstructure to its microbehavior? So, we built a little raster arm with a Panasonic remote camera head. Back then, the amazing thing that had just come on the market was an analog camera from Panasonic. It was smaller than this pens cap, the camera, and it was a little wire and it went to a special control box. So, it was this tiny camera that was full color, very, very, very highly accurate camera. So, we put this on the end of a raster arm, crushed it so you couldn't squish the bugs and designed the whole thing into a terrarium where you could put the Madagascar hissing roaches or other bugs. And then, in the corner of the room we designed a kiosk where you have a three degree of freedom joystick and a huge tube television; this is before LCD panels, so you had a huge tube television on which you could see the bug blown up to be your size. And, we put a stool there, just the right distance away so you'd fall into this experience with the joystick and we made the terrarium completely clear and positioned it so that you could sit down and drive inside the terrarium or you could stand up and look at the robot interacting with the bug and see the person and the television screen. So, you had two different views and displays, one was the telepresence display and one was essentially an art piece that showed a human, a robot, and a bug all interacting with one another in a very unusual unconventional way. And, that really worked beautifully in measuring time on task. We saw people jumping from seconds walking past the display to two to three minutes spent on the display until the parents would say really we have to go Ricky, come on get up, we have to go, enough with this. Let's go to the next exhibit. And so, we saw so this wonderful experience of people interacting with it in different ways, looking at the bugs, looking at how the bugs eat, and especially looking at the mandibles on the Madagascar roaches and how they would actually ingest the pear and cut it apart. So, we saw that kind of peculiar attention to natural detail forged by a relationship that you have to a robot that disappears. The relationship with the robot is not explicit and, in fact, it becomes part of the background, and that also set an ethical stage for our research, this idea of using robots as a tool for causing a bridging of the gap between people and the natural world where we have the robots somehow disappear into the woodwork and have what has surfaced be a relationship between a person and nature. Odd to hear because ordinarily the way you could achieve a relationship between humans and nature is you go outside. You go walk. You go use your senses. So, the challenge for me was as an innovator or an engineer is there something we can do with technology that, in fact, can amplify that feeling we get in nature and is useful rather than deleterious to the fact that we want people to spend more time outside and less time with technology. 

### Challenges of Robot Interaction

Selma Sabanovic: 

And, what kinds of technical challenges or innovations came up once you started working much more closely with people and robot interaction? 

Illah Nourbakhsh: 

Part of the challenges that we started facing were that neither human factors, nor human computer interaction had really figured the aesthetics and the social design of robots, physical models. HDI had done it for the flat screen on the computer, but it doesn't apply directly to robots. There are social inhabitants of our space. Human factors had worked it out for complex machinery, like a Boeing 747, but that doesn't work for untrained humans interacting with an object for the first time. It's really quite complex, like a 747. So, one part of the challenge is that we saw the need for multidisciplinary design teams to work together to be able to yield a product that had true value. And, to that end we had to put together a lab that had this absurd collection of skills and talents. We had to put psychologists and curriculum designers, in the same room was a graphic designer, a material science engineer, a mechanical engineer, an electrical engineer, and we had all of that in one lab at one time. And, of course, we had to have firmware coders and hackers and software enthusiasts and AI experts. So, that was the biggest challenge was how do you get all these people in the room at the same time and then talking in the same language well enough that they can in a cross disciplinary sense build a robot that weighs on all of their disciplines equally rather than being this rousing demonstration of some one thing like look it never get really well and we're going to ignore everything from aesthetics to human form to factor to long-term educational impact. How do you do all of it? That was one big problem that we faced. The other big problem we had was sustainability. We didn't want to do projects in which you demonstrate a robotic artifact, for your funder, and then put it on the table or the shelf and then move on to your next project where you demonstrate a new artifact or a new funder. That's a common theme in many of the engineering and science disciplines where you're essentially driven by the need to do a good demo because a demo brings in the money. And then, the money brings in a new project and you forget about the old project. Our question was fundamentally if we're trying to measure social impact it has to be long-term, so how do we create a funding architecture in a lab that can sociologically support people taking risks, doing work that isn't milestone or deadline driven, and then rolling things out that are affordable. And so, the tact we took was no defense funding, no contracts, only gift funding. And so, that was really difficult because I had to go out and raise a whole lot of gift money from foundations, from corporations that ordinarily want some kind of contractual arrangement explaining to them I don't want your contract, I'll take your gift money, but don't worry I'll open source it so you can use it. But then, anybody can use it and that was really the challenge of running the thing. Put the skills together to the people and then get the money to be clean money, not encumbered by milestones and driven by the defense department, so they have clean money, interesting group of people, and now you can take on new high risk projects without anybody telling you what to do on the outside, and that's where we've gotten to over the years. That's really exciting and different. 

Peter Asaro: 

So, what were the challenges of convincing the companies to do that kind of gifting and what were the arguments you made that changed their minds? 

Illah Nourbakhsh: 

It's interesting because the companies, everybody assumed what was wanted first was the reason for the licenses so the supposition by the technology folks and legal folks at Carnegie Mellon from day one was the companies want license agreements; that's why they fund us. They want to use it and own it or at least have exclusive rights to it so they can have a competitive advantage with it. But, we meet with them and literally I remember with Microsoft, we met with them one time, and they said we'd like a first letter for refusal and a license to your educational robotics technology that we're going to fund and our lawyers were in the room and their lawyers were in the room, and I said actually we don't do that in my lab, but I'll tell you what we will do, we'll make it a gift, you guys give us an unrestricted gift. We'll get to use all the money as we see fit for educational robotics and I promise to open source it all so you can use it anyway. And, I could see my lawyers feeling like oh no, now we're going to have this debate about ownership and actual property and the Microsoft folks said oh yeah that's fine, we just want to make sure we can use it. And, we all nearly fell off our chairs. It was this realization that the companies aren't trying to establish competitive advantage with the universities, they're trying to further themselves. They're trying to lift their world, their industry themselves. They're going to have a competitive advantage because they have interaction with us because they have a personal relationship. So, they're going to have that anyway and they get that they're investing in people, not ideas, and so their relationship with people is all that matters. And so, when you tell them we'll open source it and you can use it, don't worry, we'll make sure you can use it. We'll help you use it; they were fine with it. And, this happened with Intel, with Microsoft, with Google, and to me what was interesting was we had to change a bit the mindset of the tech transfer folks here. But, as they saw things like CMU Cam and Palm Pilot Robot Kit and the museum work take off, they got that we were a low cost investment because they didn't have to go after patents for us. They didn't have to file suits against anybody or create complex legal agreements and so in a way letting us run it this way was cheaper for the university and they could see that we were establishing good relationships anyway. 

Peter Asaro: 

So, what were some of the... 

Illah Nourbakhsh: 

Bad news, it's 10 o'clock. 

Selma Sabanovic: 

I know. 

Illah Nourbakhsh: 

I'm sorry guys. 

Selma Sabanovic: 

Okay. 

Illah Nourbakhsh: 

There's like 50 other projects, the problem is. I mean... 

Selma Sabanovic: 

### NASA Sabbatical

I guess the one other thing that I was curious about is NASA because you spent some time at NASA doing work, so what kind of work did you do there and also who were the people that you interacted with there? 

Illah Nourbakhsh: 

Well, I've been lucky to get offered multiple sabbaticals over the years from Carnegie Mellon. On one of the sabbaticals, I went to NASA ING. I was recruited by Dan Clancy back then. He was running a large portion of intelligent systems work at NASA AIMS. And, we moved there for a year and a half, and, in fact, I had my first daughter there, my first child, my daughter there, and lived in downtown San Francisco, which was fantastic. It was an exciting time to go there because of two things that were happening. One, the Mars Rovers were landing and so what a perfect time to be in the excitement of NASA. Two, we had started a major project where we wanted to actually create a Mars Rover like experience at museums all of the country, so that people could see what it's like interacting with a robot doing science, and again it was the same ethos. We don't want you to just play with the robot, we want you to be a scientist, wear a white lab coat, imagine looking for signs of life in a rock yard. And so, we wanted to create a robot experience that gave you that scientific experience as closely as possible that you could feel the quest of science looking for life doing a chemical test on a rock. So, it was perfect because I was at NASA. We were doing the educational deployment. We were working with the Exploratorium, which was right there at the National Aeronautic Space Museum on this side of the world, and I was able to be in the middle of the hubbub of the NASA landings. My job there was to be lead of robotics for NASA Ames. So, I was directing a group called Intelligent Robotics Group, which is the principle robot group within NASA Ames and so as part of the lead position there I was trying to track a course for how our group goes, what projects we do. I was working on the 30 strategic planning effort for NASA, in general, the NASA Headquarters. And so, it was really an exciting time to understand NASA, learn about the goods and the bads in government work and government funding, but also be so close to the action that I could do my best possible job directing our educational robotics work with the part of the personal exploration robot that we ended up deploying to a number of science centers. 

Selma Sabanovic: 

And, who did you work with at NASA? 

Illah Nourbakhsh: 

The Robotics Group included fabulous people, Randy Sergeant, Ann Wright, Matt Deans, Liam Peterson, Susan Lee, the list goes on and on. I had something like 25 or 30 people in my group. And then, above me, there was Jimmy Crawford and above him David Korsmeyer and above him Dan Clancy. So, that was my chain of command so to speak, and it was fabulous. They are people who are genuinely interested in furthering human knowledge and figuring out how humans and robots can together go back to places like the moon and Mars, which is constantly influx. I mean the chance of this happening varies from 1 percent to 5 percent and goes back and forth bouncing around. 

Selma Sabanovic: 

And in terms of the 30 year plan, what were some of the points that... 

Illah Nourbakhsh: 

The end of the 30 year plan, at that point, was we were just about to take off and go to Mars with human flight. The exciting part for me was we were going to go to the moon and take the lunar regolith, the lunar soil, center it with a laser and that makes concrete. It makes great concrete, 2000 PSI concrete, so we were going to make concrete structures on the moon, all with robots. So then, when the first next astronaut lands on the moon they go inside and take their helmet off and they're home. That was the dream that I just found remarkable was that they were going to have a robot factory making housing for people on the moon. So, that was good science fiction. I really have to go. I'm so sorry. 

Selma Sabanovic: 

No, no, no, no, no, this was great. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Illah_Nourbakhsh&oldid=182653 "
