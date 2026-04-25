1 About Jun Ho Oh 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 First Robotics Project 4.3 Industry Work 4.4 Robotics in Korea 4.5 Humanoid Robotics Project 4.6 Open Source Robotics 4.7 Humanoid Applications 4.8 HUBO 4.9 Military Applications 4.10 Other Robotics Projects 4.11 KAIST 4.12 Perceptual Systems 4.13 Advice to Young People 

## About Jun Ho Oh

Jun Ho Oh was born on October 3rd, 1954 in Seoul, South Korea. He received a BSc and MSc in Mechanical Engineering from Yonsei University in 1977 and 1979, respectively. He briefly worked for the Korea Energy Research Institute before entering the University of California, Berkeley where he earned his Ph.D. in 1985. Following graduation, he returned to Korea as a Professor at the Korea Advanced Institute of Science and Technology (KAIST); a position he continues to hold today. Professor Jun Ho Oh also serves as Director for the Humanoid Robot Research Center at KAIST, and is a member of IEEE, ASME, and the National Academy of Engineering of Korea. 

With research interests in robotics, mechatronics, and automatic and real-time control, his contributions to the field include the development of the first Korean Humanoid Robot (HUBO) in 2004, followed be a series of other humanoid robots. Other accomplishments include his involvement with the winning KAIST robot in the DARPA Robotics Challenge in 2015. 

In this interview, Oh discusses his interest and career in robotics, in particular the HUBO project. Outlining his involvement with various robotics projects, he goes on to describe the state of robotics in Korea and its future development and applications. Additionally he provides advice for young people interested in a career in robotics. 

## About the Interview

JUN HO OH: An Interview Conducted by Peter Asaro and Selma Sabanovic, IEEE History Center, 15 May 2012. 

Interview #723 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Jun Ho Oh, an oral history conducted in 2012 by Peter Asaro and Selma Sabanovic, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Jun Ho Oh 
INTERVIEWER: Peter Asaro and Selma Sabanovic 
DATE: 15 May 2012 
PLACE: St. Paul, MN 

### Early Life and Education

Selma Sabanovic: 

So if we could start with your name and where and when you were born. 

Jun Ho Oh: 

Okay. My name is Jun Ho Oh. I was born in Korea on 1954, October 3rd in Seoul. 

Selma Sabanovic: 

And could you tell us a little bit about your early education and how you got interested in robotics? 

Jun Ho Oh: 

Yes. The, I was educated in Korea; I got my Bachelor Degree in Yonsei University, Seoul and Master’s Degree in same university in Seoul in the field of mechanical engineering and it was year 1979; I got MS year 1979. And I worked for Korea Energy Research Institute for two and a half years and then I left my country to the United States for my Ph.D. degree and I entered the University of California at Berkeley and I got the Ph.D. there in 1985. And I returned back to my home and I became a professor at KAIST-– Korea Advanced Institute of Science and Technology. Since then I still be there. Okay? 

Selma Sabanovic: 

Mm-hm. And when you were in Berkeley who were you working with? 

Jun Ho Oh: 

Yes. My professor was Masayoshi Tomizuka in mechanical engineering department. I met him yesterday. He’s around. <laughs> 

Peter Asaro: 

What was your research thesis? 

Jun Ho Oh: 

The title of my, the thesis was adaptive control of milling machine. I guess, am I right? <laughs> It was 30 years ago so <laughs> I forgot the exact title of my thesis. 

Selma Sabanovic: 

And what were some of the problems that you were working on for your thesis? 

Jun Ho Oh: 

Thesis? 

Selma Sabanovic: 

Mm-hmm. 

Jun Ho Oh: 

We try to automatize the milling process for medical team. We have to decide so called the turning speed and feeding speed and that depends on the material to be cut and the size of tools and accessories, etcetera. And in these certain level we explore to decide correct one. And even the depth of cut is varying we have to change; we have to find alternate value for the best cut. And my research is ultimately find the kind of feed rate by self; by measuring the force, the cutting force and by varying cutting force by changing the cutting speed we can get very smoother and very even surface with single cut. 

Peter Asaro: 

Now what first got you interested in mechanical engineering or when did you first realize that you wanted to be an engineer? 

Jun Ho Oh: 

I was born as an engineer and scientist. I played with many gadgets and break everything. I start to fix someone, something but eventually ends up with all break everything. <laughs> And I built my, many toys, I didn’t buy; I just by, I just made by myself. And I was very interest in electronics and the, I assemble and disassemble. Made my radio, walkie-talkie and audios and I make many stuffs so I eventually I become engineer or scientist. And also I like more physical devices so just tangible. So that’s the reason I guess I choose the mechanical engineering department. 

Selma Sabanovic: 

How did you get the knowledge as a child to work on some of these things? 

Jun Ho Oh: 

Yeah. I think it’s by curiosity. I learned by myself and if I got a curiosity I have to solve the problem by any mean; so by break or read something or ask or mostly find by myself. Usually I am, I was a little bit shy to ask things to others so I try to find by myself. So that’s one of the way and by that time it was about say 50 years or 55 years ago so there’s no internet and there are not many books. So during, when I start to read something I start to read the encyclopedia so I read, I read encyclopedia more than say 10 to 20 times. So the, when I third grade in elementary school I read only I could understand, I skip; I just watch the pictures. And next year I could read, understand a little bit more and in high school I just read like surfing; just read then, just the same as you know <laughs> surfing in internet. 

### First Robotics Project

Selma Sabanovic: 

Sorry, go. 

Peter Asaro: 

Oh. What would you consider your first robotic project to be? 

Jun Ho Oh: 

Actually I didn’t do many work explicitly on robotics because the motion tool I did it with, I did it with the milling motion, it's a motion tool, sense motion is ultimately motion programmable. But that is robot actually, but that is robot, but functionally it’s a robot. And my background to deal with that is ultimate control. Okay? So ultimate control and sensing and micro – built-in control and motion tools; the combination of those stuff would be a robot because robot is a new creation to do special things. So before I building my first robot in the year 2002 my most interest was to realize the control in the real field; I try to implement all my theory into real thing. So naturally I did research related on robots but not essentially robots, for instance servo controls and sensing eventually became a robot. The reason I decided to build human like motion is that I watch the TV, I <inaudible> a human robot, the world, I just basically say that I could make it because it’s just a machine. So yeah, someday I’d make it because there’s no reason; just for fun and for the achievement by myself. So I apply some fund to build that one but no one trust me that it’s impossible to build just this kind of good nice robot. But they spend millions, millions of dollars for 20 years. How could you build it in a year with the fraction of just less than one percent of money? So I thought, I understood that because it’s the natural way to think like that way. So I self-funded; I started only from $50,000. I built my first robot in year 2002, I show to my colleagues and I got a fund from my institute and then I make second one and in third year the government approached me and they decide to support me. So I got about a half a million to start fund that first year, I made my first human robots. That’s the start. <laughs> 

### Industry Work

Peter Asaro: 

And before the humanoid project were you doing a lot of work with industry? 

Jun Ho Oh: 

Yes or not. Because it, it is not generalized, it's my own case. I usually I, usually I like enjoy my life; enjoying life means that playing, does not mean that playing go outside. It’s just I do the research for my interest and for my fun in many cases. So my, for example one of my examples that I make is the autopilot thing of helicopter. No one is doing that one so it was late or early ‘90s or late ‘80s. Just it was part of my hobby and there’s no fund and in that sense I did many practical work but something not quite related in the interest of product. So in that sense I didn’t do much work with the industry but other sense that I like practical work so I worked with many medium size industries. 

Selma Sabanovic: 

What were some of the companies that you worked with? 

Jun Ho Oh: 

Say aluminum tubing company for example and sewing machine companies that they automatize their process sometimes. 

Selma Sabanovic: 

Mm-hm. And what were some of the projects that you worked on and the kinds of problems that you were interested that were fun for you in these…? 

Jun Ho Oh: 

What you say? 

Selma Sabanovic: 

So what were some of the problems that you were working on in these projects that were fun and interesting for you? 

Jun Ho Oh: 

Yes. Actually the, as I mentioned before, that I loved to realize something in the book so project with industry means that the, I could implement the ideas and theory into real world. That is fun. So it may not be very difficult problems but very practical problems. So I love to solve very practical problems; this not in the book but I can make use the knowledge learned from the textbook. It’s not easy actually, not easy; is very practical problems is not easy. So I like that kind of challenge. It’s a human robot; it’s kind of result of some kind of challenge actually. 

Selma Sabanovic: 

Can you tell us a little bit about one particular, or one or two particular projects where you worked through this challenge and how you did that? 

Jun Ho Oh: 

Yes. Say for example say the tubing company; they want to have straighten the tube. Once the tube is drawn from the machine it’s twisted so it should be straightened and, with the strength. And strength motion, the strait motion is all the manual set so it is done by experience. Very experienced men can tune the old, the rollers to fit the, to make all the pipes straight. So I like to automatize that one and I like to program one. The thing is that once they set the set-up and it makes straight the next day it is not repeatable. So there’s the problem so I like to design very precise motion to repeating the setting up. Once you make it repeatable then you will have statistics and you can formalize your experience. Okay? Then the next step you just read the chart and you can reprogram it. It doesn’t need to be very smart but if you have the chart and you can look at the chart and you can reproduce and you can modify from that base. So something like that for example say. 

Peter Asaro: 

And what motivated you to work on the helicopter autopilot? 

Jun Ho Oh: 

One of my hobby, I have many hobbies, but one of my hobbies was playing with RC <laughs> planes and motor boats. Sometimes I was just, just, I got the error <laughs> that, oh yeah helicopter. So I try to learn the helicopter hovering but it very hard to make helicopter hover because the helicopter is naturally unstable. So we have to, it’s similar to I have to do something like that but it’s much more than that; double pendulum type things. So you need lots and lots practice to make it hover. I hate to practice type of things so first I design is that simulator. By that time there’s no such thing simulator. At 25 years old there’s no fancy graphics so I made my own simulator because I know how to interface with computer. I know dynamics, I can, I know how to make some graphics so I made very simple simulator and I learned through the simulator because I use real, easy break; very easy to break. So I learned, so I learned the hovering through my simulator and then I tried real one and I found that why do I have to do that? Camera could do that. So I started to put camera and then naturally made the hovering. So I wrote the paper, not general paper, a conference paper and it was almost first, the paper related on hovering, so still nowadays the researcher who is studying hovering they refer that paper sometime. Not every time. <laughs> 

### Robotics in Korea

Peter Asaro: 

And more generally, could you tell us a bit about the field of robotics within Korea at large and what it was like there when you were a student? 

Jun Ho Oh: 

Yes. Say that the, Korea is industrialized since 1970s; so very late. They become more high tech related, industrialized on, somewhere around ‘80s. So the ‘80s is the end of development of industrial robot. So in leading, technology leading countries like Japan, United States and European countries they already have many, many robots, industrial robots, and they don’t need to do more research on their own because all the technology is saturated and the only thing what they do is that they utilize it. That was what happened in ‘80s. By that time in Korea, in Korea it's an economic boom there so we have say automobile company, they build their own factory and the Samsung electronics they need robots. So Korea needs lots and lots of robots to build their factory and it’s kind of <inaudible>, so called auto, the automation period; CIM, Computer Integrated Machine. They are very common language in the industry, like these days like nanos and bios; by that time the world's automation, in the world and Korea is the same. So we import many robots and naturally we start to learn what is robot so they went out to learn robot. But in western countries or leading countries they don’t work on robot because all other research is over on that area. What they do at that time is intelligent interactions and service robots. It’s far away from the industry robot. So the older Korean scholars went out, on that time they learned about intelligence interactions and kind of robot operation technology. So what happened is that in leading countries they build a house of the intelligence under the basement of good systems and good knowledge of pressure machining. Okay? But in Korea we learn same thing but there's no base actually; we don’t have any system engineering. So at large I guess if you ask the Japanese what is robot they say that it might be, it’s making a product; it’s a machine. If that same case to Korean people they say luxury products. <laughs> It’s a toy or some, they cleaning robots and something like, kind of like home appliance. That is the thing. So in fundamental system and the high tech pressure machine in terms of, on that view we cannot catch up the leading countries; they’re very strong and they have 100 years of history. In that area, because we're weak but in new, newly made direction of robot like intelligence and service interaction type things we are in, yeah we’ve, we work with same shoulder. Mm-hmm. Yeah, we work together so that’s the reason we change idea and I could present my paper here. And also the size of market, consumer market, I think the Korea is ranked as maybe fifth in the world so we are using many, many robots. And the government realized that the robot market is very big and we lost first part industry but now, then we can catch next generation of robots; service robots. So the government decided to put more research money on that area so since past 10 years and government has reasonably good support for the industry and the universities to catch up, finish robot. 

Peter Asaro: 

Were there any particular series of events that led the government to embrace service robots or…? 

Jun Ho Oh: 

Yeah, service robots. The, in worldwide, robotics market at this moment is divided by several applications; first biggest one is military applications dominated by United States. Also medical approach also dominated by United States. And service robot, so the Korean government think that the service robot would be a good candidate so they decide to make service robot and they invest service robot area. But thing is that who would be the user? So normal people. The expectation of service robot is very high; they want have service robot to cook or clean everything. But in reality there’s no such kind of service robot. So the thing is that we make service robot but no one is using that one because he can't do anything just saying “Oh, hello.” <laughs> “You have mail,” I know. <laughs> Something like that. So now the, I think that, it’s my opinion, that the <inaudible> tech robot more applicable for the elderly society because everybody is concerning the elderly society; will be coming in 10 to 20 years by the time they say aged person will be very many. Somehow they might be supported by, helped by somebody, by some devices maybe. The thing is that there are two problems kind of population ratios of who will support them, they have to work. Secondly, even though they have money to hire help as a maid but it does not guarantee that he can keep the dignity. So what they want, I talk with the really disabled person is that what they want is they want to drink by his own will, by his own intention. They hate to ask "Please bring my…" one of, say "bottled water, 2 a.m. I want to go toilet, 3 a.m." Wake him. And "I wash, I want to wash." What they want is "I want to wash when I want by myself." Who will take care of you without degenerate the dignity? The robot is the only <laughs> option I guess. So Japan has realized that I guess so that’s the reason that Toyota and Hyundai is investing many money on robotics, especially home service robots. If I see their products and it’s quite many related in with the elderly people I guess. 

Selma Sabanovic: 

And in Korea also are the elderly people something that is a focus or are there other groups? 

Jun Ho Oh: 

Yes, focused, focused. But not that much as Japan because Japan there are many government money but also there are many, monies are for the major big company like is Honda and Sony are in need and Toyota and so many heavy industry companies. I knew that they invest big money on that area. But in Korea the, say Samsung and Hyundai, they don’t do. They may have their own research group in the world but they going invest big money and they never invest money in the <laughs>, in the university to have good robots. And there are medium and small size robot companies in Korea but their product is simpler for education, and cleaners, and some kind of Lego like devices. 

Selma Sabanovic: 

So is most of the funding from the government? 

Jun Ho Oh: 

In… 

Selma Sabanovic: 

For robotics? For smaller… 

Jun Ho Oh: 

Oh yeah, yeah. No, there are, there are, there are but the market is not very near yet. So the industry you got, usually when government put money on the area they want result in five years all the way. They are always saying the long term but they want to see the results very soon. So this the reason they know what’s necessary, what we have to do, but if I say that it’ll take 10 years, 20 years then they say no. <laughs> Okay? That’s the problem. So they know that they are needed on their area but few companies, some of company are doing but they don’t, they know that it’s not made money in quite near future. 

Peter Asaro: 

And in terms of the academic research, robotics is a very interdisciplinary field. 

Jun Ho Oh: 

Yes. 

Peter Asaro: 

Are the research centers at KAIST and the other centers around Korea focused within specific departments or general? 

Jun Ho Oh: 

Very wide, very wide; very general, so very general. No specific because the interactions, intelligence, visions, navigations and emotion, any of it, languages and many are all spread out; all spread out. Very similar to any other countries, all spread out. The reason is that nobody knows which one is mainstream because there’s no tangible robot yet. So actuator is important, combination, intelligence, everybody is do, we have to do everything at the same time. So we have research center in KAIST but they are doing all different things for different purposes and government funding also same. Because all the specialists say that they "My part is most important." <laughs> There’s no proof. So mine is important. So they cannot make decisions. Okay, you share. <laughs> That’s the way. 

Peter Asaro: 

So can you actually get a degree in robotics or do you get a degree in the other fields? 

Jun Ho Oh: 

Yeah. Me? 

Peter Asaro: 

Well you or your students. 

Selma Sabanovic: 

A student in Korea. 

Peter Asaro: 

Students in Korea. 

Jun Ho Oh: 

What do you mean? 

Peter Asaro: 

Can you get a Ph.D. in robotics? 

Jun Ho Oh: 

Yes, yes. Yeah, yeah. 

Peter Asaro: 

In robotics but not just mechanical engineering? 

Jun Ho Oh: 

Oh no. Some university has named, the department is robot engineering or robot science; some robot, what’s that, yeah robot engineering department for example say. It’s kind of fashion; in 10 to 15 years robot has become very, very popular so many university change the name that it might just. Even in Korea robot high school, we have robot high school in Korea and robot department. But what, and become department of mechatronics for example say. But then 80 percent of the course material is the same as, became kind of mixture of mechanical engineering and electrical engineering; a mixture. The thing is that as you mentioned the robot is interdisciplinary and also it combines many different practices. Once you became good experience and knowledge in robotics means that robot is combination of, say for example say mechanical design some software and something. Means that everything, automobile, is that. Camera, that. So even though he got degree in the field of robotics they don’t need to be robotic engineers. In any company they want to make the automation lines, the old knowledge is from robotics. So robotics is kind of learning tool, learning base, mixing bowl. So the, for example say my student, I am in department want to become engineering and also in KAIST we have so called robot major program; so they can get Master’s, not undergraduate, Master’s or Ph.D. on that area. That does not mean that they are going to go to work at the robotics company. They go to Samsung Electric Hyundai and ship building companies. What they want in their companies is the same; they want to design some motion, they want to control it and to control it they need some formula. What’s that? That’s robots. Robot doesn’t need to be a specific shape or function; it’s just any, any motion with certain level autonomy, certain level of control <laughs> and a communication form there and mobility. That’s it. 

### Humanoid Robotics Project

Peter Asaro: 

So can you tell us a bit more about how you approached the humanoid robotics project? 

Jun Ho Oh: 

Fortunately I got fund from the government and thus far they support me without any question. Okay? So as long as I produce something and they be satisfied they do not check how many papers do you write, how many patents did you have to make; they do not care because I showed good results all the way. The program is almost end, this year’s the end of the program so I have to find new fund. So during past 10 years I was very happy to do the research what I want. So yeah, that’s it. 

Peter Asaro: 

Well what were your goals for the project? I mean there’s been other humanoids. What was gonna make your humanoids special? 

Jun Ho Oh: 

Yes. The, there are human robots in the world and most of them are in Japan and the famous one is Asimo and HRP2’s and some, the famous robots in the University of Tokyo and other places Waseda, Osaka there are many. In Korea we have a couple of models and the States, Europe they have a couple models. But thing is that if you want to buy human robot it’s deliverable. I think HUBO is the only deliverable robot in the world. So we already deliver seven HUBOs in the United States, two HUBOs in Singapore, now we are preparing three HUBOs for, one for China and two for other Korean institute. The reason that the human robot is hard to sell is that the robot is very sensitive and naturally unstable so you power off it means they broken, just for now. Simple just disengagement of cable ruins everything because naturally unstable. Like as Phantom or the F50 Fighter lose one leg, one wing, it just completely – it's just over, right? Same thing. And this is permanent setup so this very difficult to keep in good shape because if made visible – and there are so many parts and each goes wrong without any fault, without any mistake. So if you sell one robot how could you maintain it? So my part is that when someone buy my robot then I invite them, him in my lab and give all the material, parts and let him assemble his own robot and dissemble; assemble, disassemble. Okay? Take it and keep, do it at your home. So to do that I have to release a level of technology that I have and I have to instruct them how to program and how to, what is internal structure and working algorithms. There are many know-how’s. There is some level of know-how’s will be released. But I take the risk because without taking such kind of risk I cannot deliver anything because they can do anything with the robots. So I encourage them to modify. I ask them just increase, open the shell, on it's open platform and you could do research with this platform. So what I want eventually is that I want to be, my robot to be kind of standard research platform in the world who want to study only with <inaudible> robot or with human robot. That is my goal. So I open the enterprise named "Rainbow Company." I have the open license from KAIST. So KAIST shares 20 percent of stocks and instead I could use all IP’s related to HUBO; developed in the KAIST institute. So my immediate goal is build and design and improve HUBO to be more reliable and robust; to be used by anybody. So that is not easy, very, very tough. So I’m spending many, many time to achieve that goal and that goal will be in couple more years. Yeah. 

### Open Source Robotics

Selma Sabanovic: 

I was just gonna ask because you were mentioning open source and Willow Garage is also very interested in… 

Jun Ho Oh: 

Yes, I know. 

Selma Sabanovic: 

...having this open source notions of robotics, Especially with ROS, the operating system. 

Jun Ho Oh: 

Yeah, yeah. 

Selma Sabanovic: 

How do you – do you see yourself as being in anyway in competition with them? Working together, or... 

Jun Ho Oh: 

The – thus far, I was very independent. The HUBO project, I’m the only one. I’m the only one who is responsible for the HUBO project. For example, Asimo, any other projects, are the result of a big group. So there are so many authorities. There are so many stakeholders. But in the case of HUBO, I’m the only one. I’m responsible for that. If I made decision, that's the final decision for the HUBO. And I’m very independent. So I’m using my own say, architecture, <laughs> my own thing. And the – yeah someday, and not today, maybe not tomorrow, but someday, but maybe next year, I may use ROS and if I believe that it’s convenient, and yeah. 

Peter Asaro: 

More generally, do you see open hardware platforms and open licensing as being a crucial way for robots to proceed? 

Jun Ho Oh: 

Maybe or may not be. The reason that I’m saying is that the robot market, big market, I think that we have to wait a little bit more, okay. So say, in 20 years, the – some robot companies made very many IPs but all – most of them expired before commercialized. So I think there’s still that kind of thing will happen. So, in some sense we are in the same boat, same ship. So all the ship will sunk – sink, okay. So I think that at this moment, there’s some technical things may be hidden but the general thing we may share, I think that’s the common practice accepted at this moment. So, the – I open my platform is that, yeah, I could produce my own maybe, two or three or five units a year. Not 1,000, not 10,000. So it is not a big market, it’s a good market for me, for example say. So nobody much care about IPs or a simple, very simple general one. So I think that the – at this moment, important thing is that we have to make good example of success story for everybody. I think that’s – so the very leading and the academic base knowledge, we are all shared. We all share, okay. We have all the same thought all the way. What is clever, what should we do? The all the robot engineers are constantly same thing, they are squeezed, they are asked if their government and funding agencies, they always say, “I support you for 10 years what did you make?” They are all questioned, in Japan, Korea, all the same, all the same. 

### Humanoid Applications

Selma Sabanovic: 

And how do you see humanoids in terms of application. Is it mostly for research? 

Jun Ho Oh: 

I guess research, research and exhibition and for fun. 

Selma Sabanovic: 

And what are some of the things that you think are interesting? 

Jun Ho Oh: 

And also, yeah, also the – it can be used for kind of technology testing vehicle. So for example say, certain motorist survived, on humanoid robot means a very good one, okay. It’s actually the same, better than same, because it is in very harsh conditions all the way. And then to make say the <inaudible> structure to be fit for such kind of purposes, that part must be very good. So I think the industry is kind of spin out or spin off during the process of developing such kind of robot and playing with such kind of robot. Is one of the by product, I guess. That is an important things. 

Selma Sabanovic: 

So the humanoid is kind of like a grand challenge? Basically? 

Jun Ho Oh: 

Yeah, yeah. Itself is grand challenge, yeah. 

Peter Asaro: 

But you also see a certain practical applications in the future for these kinds of robots? 

Jun Ho Oh: 

Yes. Therefore human robot, for example, DARPA Challenge, Grand Challenge they did not say, it should be a human robot, but it all seem to be a human robot, I guess. Say that we don’t use human robot to close a valve over there. But, the military or disasters situations say there are some radiations and bombings and you have to close a valve over there, 10 million bucks robot, humanoids just crawling very unstable. But if still he can solve the problem, they will pay. Because then they’re usable, useful. I think it in certain period of time, human robot will be something like that. Very expensive and nobody can use it because it’s dumb. So unstable but very small niche, they will pay for that. Thus far, we don’t have any such kind of robot yet, but in near future, maybe five years, we may have that kind of things. But not be used for general, but still some very small niche that will be necessity and they might be successful. 

### HUBO

Selma Sabanovic: 

Have you had any spin offs come from your work on HUBO? 

Jun Ho Oh: 

Yes. For example say sensors, yup, and arm. Can separately sold. And force sensors, and finger. Some ask me, “How much?” So I said, “20,000 bucks.” They say, “Cool.” <laughs> So and the <inaudible> boards and some pressure control technology. I made the telescopes and the very precision one. So all the same. The HUBO and telescopes and any other things, all the same. The shape is different but technology same. So, yeah, the HUBO is one example of that kind of complex system. So the spinoff is trivial, naturally done. 

Selma Sabanovic: 

Can you tell us about the things you developed in HUBO that are different from other humanoids? Such as ASIMO? Or... 

Jun Ho Oh: 

I don’t think it’s not very special. I use very common techniques, technologies, thing is that, only big difference. Very big difference, is that I did it by my – alone, in very short period of time. And I proved that it can be done by one person, with very short period of time, with very limited budget. Before that, we were educated that – by Japanese – that if you don’t have any billions and billions of money and plenty of time <laughs> and plenty of things, don’t try to do that. That we were educated since several – tens of tens of years. So I break the law. <laughs> 

Selma Sabanovic: 

And who are some people that you worked with on this? 

Jun Ho Oh: 

Who? 

Selma Sabanovic: 

Did you have any collaborators? I mean, you say you were doing it alone. 

Jun Ho Oh: 

Yeah alone. Yeah, my students, that’s it. 

Peter Asaro: 

What were the biggest challenges that you faced as you built it? 

Jun Ho Oh: 

At first, no one trust me. Okay, even my students trust me, okay because the – there are tons and tons of paper related to – how to make it walk. Tons and tons of paper and the thing is that all – discard all the papers, okay. I will start from scratch, okay. That is very hard. Still very hard, still yesterday night, I argued a lot with my students. Okay. So the – in the previous days material you’re wrong, I have to right that. He said, “I break the common law. Why do you have to do that?” It’s fun. <laughs> 

Peter Asaro: 

And did you approach it with more the passive dynamics of walking or did you use active walking? 

Jun Ho Oh: 

Active, active, no passive, all active, yeah. Yeah, I’m trying little bit passive, but basically active. The reason active – all the way means that these days, the – I’m little bit hard part. Now the soft computing and software and intelligence and many other things, we can distinguish what is industrial robot and non-industrial robot, service robot. The thing is that industrial robot is very rigid, hard and deterministic and repeating, just no autonomy. The other one is all the other way, okay? Lots of peoples are talking robot, interior service robot, but in these days the actually so called service robot in this day is actually very close to industrial robot. For example, say da Vinci robot, they're industry robot, and <inaudible> robot. They’re all industry robot. The field is the all go from factory, and working over there but please – basically all the same. So only thing that is not very rigid – and the more the autonomy depend on is cleaning robot. Except that – or toy robots. Some education kit, okay, they’re very soft, but the other serious applications all very hard. So thus far, I don’t trust much about such kind of soft things. Yeah, it can be applicable through the very say, weak one. So that's what I call sometimes the dilemma. Dilemma in mobility, dilemma in autonomy. Means that we – good robot, good mobility, good robot in mobility means that faster and stronger. That is good robot, strong and fast. Okay, that’s good robot. And in terms of autonomy intelligence means very intelligent one is good robot. Thing is that strong robot and fast robot is dangerous, okay. And smart robot is arbitrary. It may not work on your own intention, okay. So it could – it should be anything. So the most dangerous thing is that high mobility, plus high intelligence. If mixed to one, it’s monster. For example say, there is one robot with gun, okay, motion gun and he has full intelligence, he find who is – my friend who is my – who is for – who is my <laughs> enemy. So he decide by himself, okay. Oh, you shoot, you shoot. If there is such kind of high intelligence, he made all decision by himself, with big power, how could you trust him? How could trust him? So usually, the way is that if he’s very good mobility, they lower the intelligence to general. Okay. Better than, they follow drive, only driver. He cannot move by himself, okay? But very intelligent one, very autonomous one for example, say, say, say conversation machine for example say, you can – you speak and the answer – very arbitrary, very intelligent but only – it doesn’t matter he say, he say wrong answer it doesn’t matter because there is not power, there is no physical strength. So if there is no – if he got strengths, I can’t allow 100 percent of intelligence, autonomy, okay. You could do whatever you want, okay. But if you give some power, then you have to lower the intelligence and autonomy. And that’s the dilemma. And so, thing is that – so cleaning robot for example say, what they do is that they lower the power and lower the intelligence in a certain level. So he just – no one care that he runs around the same place ten times, it doesn’t matter, okay? He missed one point for cleaning, it doesn’t matter. It crashes somewhere, it doesn’t matter, okay. That is what happened in reality. So people start thinking, dreaming that the very intelligent and powerful robot, that’s monster. We never will have it. Even for human, for example say, human is actually very strong and intention. But... 

Selma Sabanovic: 

Sorry, I’m going to have to go... 

Jun Ho Oh: 

Yeah, yeah go ahead. 

Selma Sabanovic: 

If you can talk about the PIRE grant with Paul Oh? 

Peter Asaro: 

Okay. 

Jun Ho Oh: 

Okay. 

### Military Applications

Peter Asaro: 

Just to follow up on that, so the Samsung Techwin actually developed a robot with a machine gun that’s in the demilitarized zone. 

Jun Ho Oh: 

Only develop but not implemented yet. Even the operated by remotely, he does not have any intelligence. He cannot make any judgment. He just use very – main sensors, and he can identify there are persons but he’s not allowed to shoot them by himself. Just report and even the – as far as I know, in any other place in the world they have so called, remote machine guns, but it’s not actually used. Except some – the area attack, they may use. But still very limited because I ask them to develop such kind of projects is that – it’s very dangerous because if we are on the – on board we’ve gun at the site and the decision it different from the you are at home with screens, must be different. So it might be more chance to get wrong decision at home with video monitor. So, in Techwin make such kind of devices but it’s for demo. I think they – or it might be implemented in some sense, in some area, but there is no intelligence because this very big power, it doesn’t allow any intelligence yet. 

Peter Asaro: 

I know the Korean government also sponsored... 

Jun Ho Oh: 

Yeah, yeah, yeah. Naturally, naturally it’s right way for the military applications. Yeah, naturally they make it but really implemented in the field is out of the question. Out of the problem. But anyhow, once it is implemented or located in some site, a specific site I think, I’m 100 percent sure that there is no automatic firing. 

Peter Asaro: 

Yeah, but the Korea has a robot ethics charter. Are you familiar with it? 

Jun Ho Oh: 

Yes. They claim to make that one, they give up. 

Peter Asaro: 

Yeah. 

Jun Ho Oh: 

It stopped, because they started very simple mind, but they found it’s not that simple. Even they cannot find, what is it for? What is the subject? What is object? So it’s for robot? It’s for man? It’s for manufacture? So this – so they very aggressively started with kind of robot ethics charter with several engineers, they found that it’s not that simple. <laughs> So they invited say, philosophers and associates, scientist, and I was – I partly joined the workshop and for – to make the other one is ten people say different ten words, all differently. Someone say, he’s a super human. <laughs> I say it’s just simple motion. Good motion, that’s it. Not more than that. 

### Other Robotics Projects

Peter Asaro: 

Could you talk a little bit about PIRE and the project you’re doing there. 

Jun Ho Oh: 

What is PIRE? 

Peter Asaro: 

PIRE? With Paolo? She just mentioned it on the way... 

Jun Ho Oh: 

No, no, no, I don’t know. What is it for? 

Peter Asaro: 

Do you have a joint project with someone in Europe? 

Jun Ho Oh: 

No. Paolo, no, no. I wrote, kind of the – kind of intelligent agreement when they built that robot idea, Paulo Dario, yeah. No, I don’t do work, just we – just implicitly exchange maybe. Little intention when something’s wrong we can cooperate, that kind of thing. But not explicitly working. 

Peter Asaro: 

Okay. So what are some of the other big robotics projects that you’ve worked on that you haven’t mentioned? 

Jun Ho Oh: 

Actually the – in Korea or in the world? 

Peter Asaro: 

Well, for you. 

Jun Ho Oh: 

Okay, okay. 

Peter Asaro: 

The ones that you’ve worked on. 

Jun Ho Oh: 

Yes, in the – supported by Korean government and the – my project was not independent one. I was part of big project. So, that project is so-called Frontier Initiatives in Korean government in robotics. That ends next year, <laughs> okay. And the size of that initiative is about 10 million dollars per year for 10 years. I got about half million dollars per year from that. So the project of human robot in Korea is less than one – 0.5 percent in total. But people – lots of people say that, “Why do you have to invest so big money in humanoid robots.” They believe that 50% percent government money's coming through to the human robot. Actually it’s not. I just spend, just as one of the project. One out of hundred projects, okay. But these that – visibility is so high. So the <inaudible> division, the humanoid style robots, they are more of the people are watching the humanoids and TVs and everywhere. So people say – think, naturally think that – everybody’s doing research on humanoid, it’s the easiest one. <laughs> Anyhow, so that is the big project. And that usually covers all the area in robotics from intelligence to hardware, sensors and everything. Everything. And another thing is that I was – as I mentioned that the – I sent seven HUBO’s to the United States that is big and NSF funded and that was big. 

Peter Asaro: 

Where did they go? 

Jun Ho Oh: 

One is Drexel. And six will be going say, I forgot – Carnegie Mellon, and Virginia Tech, and Georgia Institute Technology, or Southern California, I’m not sure, it’s recorded. I have to check, repeat all the names but Purdue some of them or something like that and Virginia Tech, yeah. And the two were sent to Singapore is kind of government research institute. Institute for Infocomm. They say I2C. They are playing with my robots. But yeah, but – to deliver such kind of robots in the right period, I had to establish enterprise under the – this provision my institute. 

Peter Asaro: 

So do the do the production at the institute at the institute or do you have a company outside? 

Jun Ho Oh: 

Actually we call "lab venture." So actually it’s in the campus, in my lab. So there’s no – <laughs> visible divide line or mixed. 

Peter Asaro: 

How many HUBOs have you made altogether so far? 

Jun Ho Oh: 

Thus far, maybe 12 or 13. Already nine delivered, and we are operating three. And yeah, it means 12. And we have older ones. So, maybe 15 or 16 HUBOs thus far. 

Peter Asaro: 

How much does it cost? 

Jun Ho Oh: 

When we sell, we charge them $400,000 per unit. 

### KAIST

Peter Asaro: 

Wow. Okay. And when you first got to KAIST, after your Ph.D., were there other people working in robotics there? And what were the... 

Jun Ho Oh: 

Yes, yes, but yes, by the time robotics is one of the popular area in engineering. So it was very popular. So if I major robots, they say, “Oh come on, come on, come on.” But I did not say, design robots. I’m motion tools and automations. So by the time motion tools, automation robotics. They are very popular everywhere. 

Peter Asaro: 

And so were their other researchers at KAIST when you got there that were doing what you would consider robotics? 

Jun Ho Oh: 

Pardon me? 

Peter Asaro: 

When you first came to KAIST were there other people doing what you consider robotics at that time? 

Jun Ho Oh: 

Yeah, yeah. 

Peter Asaro: 

Who was there? 

Jun Ho Oh: 

Pyung Hun Chang for example. Prof Chang, and he’s retired. Kwak Yoon-Keun. Kwak, he just retired and Kim Soo-Hyun, Professor Kim. At the time, some of them in the EE department and computer science. Yang Hyun Seung, Professor Yang, Kim Jong-Hwan, Ju Jang [Lee] and many, many. And a famous one, Jo Hyung Suck. He retired. Okay. So many, very popular at the time. 

Peter Asaro: 

And who would you consider to be the biggest pioneers of Korean robotics? 

Jun Ho Oh: 

It’s the older one. They start earlier, for example say, Professor Kwak. Yoon-Keun Kwak, he always claimed that he made first robot in Korea. 

Peter Asaro: 

When was that? 

Jun Ho Oh: 

It was 19 – early 1980s maybe. 

Peter Asaro: 

What was the robot? 

Jun Ho Oh: 

It just usual kind of – yeah, industry robot, of course. But the – maybe ‘70s, anyhow the early ‘80s all the Korean big companies start to make robot. It's easy to make robot ‘cause they buy motor, injection case, servo set. What they do is they may link between the motor and driver. So if – the thing is that they have to buy all encoded motors, injection case and servo pad they have to buy. And what they do is they make some casting to put two different motors into one, that’s it. <laughs> 

### Perceptual Systems

Peter Asaro: 

Simple stuff. Okay. In terms of like a vision and sensing for the humanoid what kind of perceptual systems have you built into? 

Jun Ho Oh: 

Yes, I call the – my humanoid robot is not humanoid robot. It's humanoid robot platform, usually say. Means that to be a humanoid robot, it should have certain level intelligence. Mine doesn’t not have any intelligence. But platform means that it’s ready, there’s camera, there’s microphone, there’s speaker and one empty computer there. So anybody who has an idea to put some intelligence on the HUBO, he just bring his own memory stick and download and run it, that’s it. So, the – in terms of intelligence for me is no, none. None, HUBO does not have any intelligence but it is intelligence ready because it’s camera, microphone, speaker, that’s it, and the empty computer with the Window XP. 

Peter Asaro: 

And does it have any touch sensors? Or pressure sensors? 

Jun Ho Oh: 

No, no, no, no, no. So, the HUBO is kind of – the open platform. They can put sensors, they can modify hands and just – I will give some CEN, control error network lines and we provide all the protocols as signals they just make their own say, protocol to comply with the existing protocol. That’s it, so, I don’t need to make everything because is research open platform. So they can put the clothes outside, they can put at the skin. That’s how what I want. 

Peter Asaro: 

And can you tell us about this hand that you brought with you? 

Jun Ho Oh: 

<laughs> For example, the – yeah this one is the one example that which reflects my philosophy of the research platform. For example say, this one looks beautifully working... and it holds my hands like this way, and formally, and beautifully. When I show this one to somebody, what they ask me is that the – can he move like this way, and can you hold this one. And do you have touch sensors? What kind of sensor? What touch sensors? If you cannot, can you get the piece of paper like this way? So they ask their thing, if I say, “No.” They’re saying, “It’s not a hand.” But my answer is different. If you build very sophisticated hand with ten to 15 actuators, it is very difficult to make something. Control itself is very hard. So what I’m saying is that, yeah I can – this hand can take 50 percent of the objects. I give up remaining 50. But I’m formally, very robustly, handle remaining 50 percent. That’s it. The common is just open and close. I can move five fingers individually so you can program five fingers, just open close very easily. And very robust and very few <inaudible> consuming. So and he weighs only 400 grams. So it can attach everywhere. So if you have built very nice hands with 10 kilos, who can use it? And with the 20 actuators how can I program it? Even they cannot catch the very simple apple. Yeah, I can do it very simply like this. So, so if you want to sensor, you put it later. Okay? If they want it – if they say that, “I will not buy if you don’t have any perfect hand. I will not buy it.” I’m not going to sell him. Because there are such kind of hands. There are no such hands. So, lots of people needs this level. That’s what I’m saying. As in terms of the number of patents and research papers, I think it is nothing, may not be nothing. But practical use it’s super. 

Peter Asaro: 

And it’s using cables? 

Jun Ho Oh: 

Yeah, cable underactuated and very small motors and all the amplifiers, current feedback... and very strong. 

Peter Asaro: 

How long did it take to develop the hand? 

Jun Ho Oh: 

How? 

Peter Asaro: 

How long did it take you to develop? 

Jun Ho Oh: 

I’m very fast. I’m very fast, very intuitive. I do not use any 3D tools. I render everything in my brain, and it’s very complicated actually. I cannot reproduce this design but it may not take less than a month, I guess. <laughs> 

Peter Asaro: 

How many parts are in their? 

Jun Ho Oh: 

Oh, you don’t believe it’s over 1,000, no 500 maybe. I did not count. I can show – in my presentation I showed all the parts, it’s – I try to count, but I couldn’t. It’s – if I count maybe at least several 100s, at least several 100s. 

Peter Asaro: 

How much does the whole humanoid weigh? 

Jun Ho Oh: 

The HUBO 2 including case and battery, 43 kilos. 

Peter Asaro: 

43 kilos? 

Jun Ho Oh: 

Yeah, quite light. They peel off the case and battery it weighs only 36, no 32 or something like that. 

Peter Asaro: 

How long will the battery last? 

Jun Ho Oh: 

Yeah, in my presentation showed that – with single charge it runs two and a half hours walking, not waiting, walking. 

Peter Asaro: 

Wow. How far can it walk in two and a half hours? 

Jun Ho Oh: 

It measured 2.5 kilos, kilometers. It’s the... yeah, its speed is just 1 kilometer an hour. <laughs> 

### Advice to Young People

Peter Asaro: 

Great. So what are your advice to young people who are interested in a career in robotics? 

Jun Ho Oh: 

To be a robot engineer, he should become a real engineer. And, yeah, that is very important. So they’re doing research and robots, doing research on airplanes, same. Firstly, he should be an engineer, at least a scientist. Means that he should not be afraid of dirty hand... <laughs> and he should love grease. <laughs> Yeah. 

Peter Asaro: 

And anything else you’d like to add you think we missed? 

Jun Ho Oh: 

Dream and have all the curiosity and when I say to my student that – solve the problem. They are solving a problem all the way. They’re solving something, but they don’t know what they solve. So all the problem is – I always saying there’s a moving target. So, to be – to be the solution – we have to find the solution all the way. Or we find the problem all the way. But you – think there is the problem but next day, it become – the problem goes away. You’re still watching this one. What you watch, just relative, all the engineering problems something like that. <laughs> 

Peter Asaro: 

That’s very good. Great, yeah, anything else that you want to talk about? How long have you been involved at the IEEE Robotics and Automation System? 

Jun Ho Oh: 

Since, when I released HUBO, so year 2004. Before that, no one knows that. Even I didn’t know that I’m a robot engineer. <laughs> 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Jun_Ho_Oh&oldid=182487 "
