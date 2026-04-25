1 Seth Hutchinson 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Graduate School Vision Systems and Robotics Work 4.3 Evolving Relations Between Computer Vision and Robotics 4.4 Early Years at the University of Illinois 4.5 Evolution of Robotics 4.6 Students and Collaborations 4.7 Conferences 4.8 90's Projects 4.9 Funding 4.10 Robotics Failures 4.11 Influences and Experiences 4.12 Evolution and Challenges of Robotics 4.13 Advice to Young People 

## Seth Hutchinson

Seth Hutchinson was born in Sellersburg, Indiana. He earned a Bachelor of Science (1983), a Master of Science (1984), and a Ph.D. (1988) in Electrical Engineering from Purdue University. In 1939 he moved University of Illinois at Urbana-Champaign as a Research Assistant Professor at the Coordinated Science Laboratory and Beckman Institute and as an Assistant Professor of Electrical and Computer Engineering in 1990. From 1996 to 2003 he served as Research Associate Professor in both labs and as Associate Professor in the same department, before becoming a full Research Professor and full Professor; positions he continues to hold to date. 

His research interests in robotics focus on vision-based control, path planning, planning under uncertainty, pursuit-evasion, and localization and mapping. His contributions to the field include over two hundred published works. 

In this interview, Hutchinson discusses his robotics career and his contributions to the field. Commenting on his various influences, projects, and collaborations, he reflects on the evolution and challenges of robotics and provides advice to young people interested in the field. 

## About the Interview

SETH HUTCHINSON: An Interview Conducted by Peter Asaro, IEEE History Center, 5 November 2013. 

Interview #704 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Seth Hutchinson, an oral history conducted in 2013 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Seth Hutchinson 
INTERVIEWER: Peter Asaro 
DATE: 5 November 2013 
PLACE: Tokyo, Japan 

### Early Life and Education

Peter Asaro: 

If you could start by telling us your name and where you were born, where you grew up and went to school. 

Seth Hutchinson: 

I’m Seth Hutchinson. I was born in Sellersburg, Indiana and did all of my university work, undergrad and grad, at Purdue in Indiana. 

Peter Asaro: 

Did you study engineering as an undergrad? 

Seth Hutchinson: 

I did. I began as electrical-actually, I don’t even remember. It was in the time when EE departments were wrangling with the idea of being electrical and computer engineering departments and I think that my degree says electrical and computer engineering, but it might say electrical engineering. I’m not really sure. 

Peter Asaro: 

When did you know that you wanted to be an engineer? 

Seth Hutchinson: 

So I became an electrical engineer because I was in rock and roll bands in high school and I blew up my amplifiers and I thought, “If I had a – if I knew how this worked, I could fix them.” I got a degree and learned that when you have a job you don’t have to fix them, but nevertheless, that’s what sucked me into electrical engineering, audio amplifiers. 

### Graduate School Vision Systems and Robotics Work

Peter Asaro: 

What was your first robotics project? 

Seth Hutchinson: 

So robotics was late for me. I really came into electrical engineering because of the audio aspect. <coughs> Excuse me. And so I was very interested in signal processing and joined the laboratory of a professor who was doing computer vision and at some point, people from Cincinnati Milacron put one of their robots in our lab. I think it was – it may have even been a donation and it fell on the new guy to make the robot do something and I think there were several of us competing for new guy status and so that was really my first project. It wasn’t at all what I anticipated doing with my degree and I looked at the robot, at that time, as a thing that moved a camera around and so you could take pictures from different locations and so that was my entree into the robotics world. It wasn’t at all in the beginning a robotics project for me. It was a vision project, but I had a robot as a tool to help the vision project and it evolved over the course of my Ph.D. work into genuine robotics, but it took some time. 

Peter Asaro: 

What kind of vision projects were you working on? 

Seth Hutchinson: 

It was viewpoint planning. It was if you see something and you don’t know exactly what it might be, where should you look from next to maximally resolve the ambiguity that you have? And it was in the middle part of the 1980s, so it was all limited by computation power. We weren’t able to do big searches over giant spaces in those days and so there were a lot of hacks and heuristics and not much of rigor, not much rigorous mathematics at all in that Ph.D. dissertation. 

Peter Asaro: 

What kind of machines and hardware were you using? 

Seth Hutchinson: 

So the computer vision system was – it was like a four foot high, about a one meter high and then some rack of video cards and I think each video card was in the ballpark of five to ten thousand dollars. So it was this enormous rack mount system and each card did some processing. Now all of that stuff fits nicely on a chip that lives in your computer and costs twenty-five dollars or something, so it was big. The computers were big. They were in different rooms with wires going under the floor to them and almost nothing happened in real time and in order to make it happen in real time, somebody had to hack the Unix operating system to make it happen in real time, so nothing was just easy and fast and efficient the way it is today with computers. 

Peter Asaro: 

Who did you work with? 

Seth Hutchinson: 

I worked with Avi Kak who at the time was really a computer vision guy more so than a robotics guy. In fact, I think his foray into robotics was not – it’s not something that kept him for long. He did it for a few years – more than a few years. He had other Ph.D. students after me, but then moved onto other things. He moves. He’s very curious and he moves a lot. He’s always learning new things, so I’m not sure he rests long in any community, but I think he’s kept one foot always in the computer vision community. 

### Evolving Relations Between Computer Vision and Robotics

Peter Asaro: 

How have you seen the relationship between the computer vision community and the robotics community evolve over the last decade? 

Seth Hutchinson: 

It really has evolved. In the beginning, the two were really tightly integrated. I think in the beginning, most computer vision people that I knew, robotics was the motivation for it and it grew out of the – as I’m sure many people have said, out of the AI labs at MIT and Stanford and Edinburgh and places like this. And so we were doing vision at the time because robots needed to see stuff. In the intervening years, vision really earned its own place and had no need for robotics at all, so there was a period of ten to fifteen years – I may have the timings wrong – when vision people really kind of didn’t show up anymore to robotics conferences because robots – in some sense, robots were moving around pretty quickly. Vision was still too slow and there was a mismatch in capabilities, probably some other reasons too. Hollywood became a very attractive possible place to take your computer vision algorithms and use them to generate virtual characters and so forth. Virtual reality became very attractive to computer vision people and if you have virtual reality, why would you ever want to trouble yourself with the reality of a robot? I can’t think of why you would, so those communities really diverged. About a decade ago, I think they started to really come back together in part because the robotics community made a really serious effort to go out and grab onto them. So for example, John Hollerbach at the International Journal of Robotics Research had a joint special issue with the International Journal of Computer Vision on vision for robots, or robotic vision. I don’t remember the exact title and I think that might have been the first really serious effort to round some of those guys up and bring them home, if you will. Although many of them were young enough that they didn’t know it was their home. <crowd talks> You should put a sign, a do not enter sign or something like that. I think that would help. <laughs> 

Peter Asaro: 

So what time did you see that reintegration taking place? 

Seth Hutchinson: 

I would say 2005s, 2006s, something like that. Isn’t that kind of the middle – what they call them the middle aughts something like that, the integration started happening again. Vision’s gotten to be really fast. I think there was a small group relative to the size of the robotics community of really avid consumers of computer vision technology to do specific tasks like tracking objects in video sequences and those guys have been consuming computer vision algorithms steadily, but not really contributing back to the computer vision side. So for example, the vision based control world, we consume the algorithms that keep track of things in the images, but we don’t necessarily produce that stuff. We take the outputs of that and use it to control the motion of robots and we tend to focus more on the control theory side than on the computer vision side. And computer vision has been fast enough to do that kind of thing for maybe a couple of decades now, but to do things that you might call scene understanding or have some general awareness of your surroundings if you’re the robot, those capabilities couldn’t happen in real time. The first really serious successes I think in real world sensor based robotics came at the end of the nineties and the early two thousands, but they weren’t using computer vision at all. They were all using specialized laser range scanners and so that wasn’t really – it wasn’t bringing computer vision people back, to put laser scanners on your robot and build 3D range maps of scenes. But things have gotten much faster and now machine learning, I think, has made a big impact in the computer vision world and you get a lot of stuff now in real or near real time that you couldn’t get ten years ago and that’s helped a lot, I think, in terms of integrating – reintegrating those two communities. 

Peter Asaro: 

What was the actual topic of your dissertation? 

Seth Hutchinson: 

It was a planning under uncertainty dissertation and it included planning sensor movements to resolve uncertainty, as well as robot actions that could resolve uncertainty and it was fairly AI-ish in its flavor. It was a very symbolic approach to those problems. At that time, I didn’t know much about geometry, not as much as I might have guessed that I knew about geometry. 

Peter Asaro: 

Where did you go after your Ph.D.? 

Seth Hutchinson: 

I stayed one year at Purdue as a visiting professor because after ten years, I had earned the right to be called a visitor and then I went immediately after that to the University of Illinois, where I have been since with the exception of an occasional sabbatical. 

Peter Asaro: 

And what year was that? 

Seth Hutchinson: 

I’m sorry, what year? It was January of 1990. 

### Early Years at the University of Illinois

Peter Asaro: 

So what kind of projects did you start when you got to Illinois? 

Seth Hutchinson: 

So down the hall from me at Purdue, not literally but figuratively, was a guy called John Feddema who was doing visual servo control, which is to put computer vision into a real time feedback loop and when I went to Illinois, I started to do that kind of stuff because when John had done it, I thought it was so cool. And so I started pretty quickly after I arrived there, working on putting computer vision into control systems and at that time, I thought I knew something about control, which was also overly optimistic and I continued at the same time working on planning algorithms. So it was planning with the aim to reduce uncertainty and I imagined a big picture where you had planning to reduce uncertainty and you put sensing into a feedback loop and so the power of feedback control further helped you deal with uncertainty and so I imagined myself as just dealing with uncertainty in an grand and global way. 

Peter Asaro: 

What kind of other robotics was going on at Illinois? 

Seth Hutchinson: 

So at the time at Illinois, there was a guy called Mark Spong that I had not met or – I think it was two years probably before I met him at Illinois and Mark really is a control theorist who does robotics and he was in a different department and so our paths didn’t cross for a long time. There was a guy called Narendra Ahuja who was more of a computer vision guy who occasionally did a robotics project and I think that was really the extent of robotics at Illinois at the time. Robotics doesn’t fit so well at Illinois. The departmental structure is very traditional in some ways and robotics is very interdisciplinary in some ways and although Illinois had a number of pockets of interdisciplinary research, there really wasn’t a robotics pocket at the time and so I think apart from Mark, I would call myself the only really robotics guy at the time at Illinois. Now there was another professional who joined when I joined, like two days before or after, called Jean Ponce who was a computer vision guy, but he did some serious robotics while he was there as well. I don’t know if he would have called himself a robotics guy at the time, but he may well have. He was coming to all the robotics conferences as well as the vision conferences. 

### Evolution of Robotics

Peter Asaro: 

How did the robotics evolve over your career? 

Seth Hutchinson: 

It didn’t evolve very quickly at Illinois. In fact, I would say it’s only in the last five or six years that we’ve built a serious robotics group at Illinois. I think in the time that I’ve been there, we’ve had a few good robotics researchers, but not a robotics – not a critical mass. I think you would not have the right to use the word program to describe what happened at Illinois in the nineties with respect to robotics. In the last five or six years, we’ve hired three or four young people who are really good robotics people. We’ve been very lucky because we’ve hired them in several different departments. For example, two of them were hired in our aerospace department – aerospace engineering department, which is not the first place you go when you look for roboticists on a college campus and yet we’ve managed to put a couple of them there. We’ve managed to put one or two on our general/industrial engineering department. You can put them in the ME department and so department heads each think they’re hiring robotics guys and that’s not necessarily the case that anybody realizes we now have too many robotics guys and you have the chance to build a program that way. But prior to five or six years ago, I think there was no real impetus on the campus at the College of Engineering level to hire robotics people. Some years ago, robotics started to look much more lucrative from a research funding point of view and I think department heads saw it as a way to bring more resources into departments and so we started hiring more robotics people and often in the smaller departments. I think you can get a big bang for your buck with a roboticist if you’re a small department. 

### Students and Collaborations

Peter Asaro: 

Who are some of the people you’ve collaborated with? 

Seth Hutchinson: 

I think Peter Corke was one of my first collaborators that was most productive because Peter’s really smart and has good ideas and is the kind of guy that takes a problem and works it through to the very end. He’s not ever content to stop at this level of abstraction if there are two or three layers below and so that’s very different for me. I wasn’t a very, “Let’s understand it to the bitter end” kind of guy until I started to work with Peter, so that was a very good collaboration. I’ve collaborated a lot with Mark Spawn. We haven’t written a lot of papers together, but the way I think about robots is really heavily influenced by the way Mark things about robots. I sat through a couple of his classes at Illinois as a young assistant professor to try and learn that stuff. There’s a guy in Mexico called Rafael Murrieta who visited Illinois for – I can’t remember if it was a two or three year period and that collaboration was a very productive one. He’s very motivated to learn new things and solve new problems and I learned a lot of stuff working with Raphael. And of course, I’ve had some really good graduate students who have taught me a lot of things along the way, as probably every professor has. 

Peter Asaro: 

Who were they and what have they gone on to? 

Seth Hutchinson: 

That’s a dangerous road to start down because the one that I don’t mention will be the one who watches this video. The ones who are probably most well known in the robotics world – Steve LaValle is very well known. He invented a thing, along with James Kuffner, called rapidly exploring random tree that I think is probably the most popular motion planning algorithm in the world I suspect at the moment. After he finished his Ph.D., he went to work at Stanford with Jean-Claude Latombe as a post doc and that’s where he met James and the two of them did this, which I think really changed significantly the way people think about robot motion planning. Maybe I should say robot path planning, but it works generally, I think, for problems with dynamics as well, although it may be used less often in that context. I have a student called Nick Gans, who’s doing some vision based control work in Texas, Sourabh Bhattacharya who did a lot of pursuit evasion kinds of work and has gone to Iowa State at the moment. I think those are probably the three most visible in the academic world robotics people. I had a student called Becky Castaño who went to JPL and is doing really cool things. I’m not sure she’s the most visible one, but maybe is the one doing the coolest things of the people who have worked in my lab in the past years. And then I think every Ph.D. student that I graduate for the next few years will probably arrive to Google because Google seems to be hoovering up all Ph.D. students. My last two are at Google now, so – I think that’s true. I should check to see if they’re still there. 

Peter Asaro: 

So can you tell me about the paper with Hager and Corke that came together in ’96? 

Seth Hutchinson: 

I could tell you, but my story will differ from Greg’s. <laughs> I honestly don’t remember the exact genesis of that paper other than Greg and I were interested in vision based control at the time and we had the idea – Greg and I met when I was still in graduate school and he was still in graduate school and he asked a particularly obnoxious question at the end of a presentation I gave at ICRA and we became friends after that. And we decided that we should try and organize a workshop on visual servo control and it was fairly popular. A lot of people came and it was really the first one – the first time that that group of researchers had gotten together, I think, and a number of people in the room didn’t really understand what it was all about. So we organized a tutorial for the next robotics conference, ICRA, and the notes that we put together for that tutorial turned themselves into the tutorial article that eventually got published in the transactions on robotics. And we had Peter Corke as the third author on that paper because he knew something about control and Greg and I really didn’t know much about control and it was just – it was a wonderful experience because Peter was in Australia and he was like the shoemaker’s elves. We would do a lot of work during the day, send him the file, wake up the next morning and he would have tidied it and cleaned it up and added stuff, so every morning it would be better than I left it the night before. And I guess every morning, he thought, “The guys in America are screwing up my good work,” so we were probably the opposite of the shoemaker’s elves for him, but that’s how it happened. It was a very cool collaboration because of the time zone differences. I think every hour of the day, somebody was working on that article for some period of time. 

### Conferences

Peter Asaro: 

So you mentioned the IEEE conferences. When did you start going to ICRA and all of those? 

Seth Hutchinson: 

My first one was San Francisco in 1986, I believe. I think that’s right, which would be almost thirty years ago. I suppose part of this process is to confront one’s own mortality and age. It was a long time ago and I think it was the second one. I’m not sure. I think the first one was in ’84, but it was in that sort of timeframe and at the time, I had no idea that it was an important meeting to go to. It was just the meeting that accepted my paper and plus it was in California, which I had never seen in my life. I don’t think I had been west of the Mississippi River at that point in my life and I don’t think I had flown a commercial airliner at that point in my life. So it was a big deal for me to go to that conference and I don’t think I realized that it would become the premiere of robotics conference some – maybe it already was at that time because there weren’t so many of them. 

Peter Asaro: 

Was there a point in which you started to identify as a roboticist or was it just some project that you did? 

Seth Hutchinson: 

I think I started to think of myself as a roboticist somewhat incorrectly in the late part of the 1980s because in the late part of the 1980s, my view of “What is robotics?” was really a small view of “What is robotics?” But when you have a small view of robotics, it’s easy to imagine yourself as king of that realm and so I thought, I think even in the late eighties, that I was a roboticist. In the early part of the 1990s, Jean-Claude Latombe wrote his famous – now famous book on robot motion planning and I had visited Stanford before that book was published for a workshop and stopped in to talk with him about it because Jean Ponce, the new guy who joined at the same time as me, had been at Stanford before and he told me, “Oh, you need to see this book.” Before that book was actually published, I had a PDF of it and taught a class from it and that really changed what I thought robotics was quite a lot and so I tried to learn those things. And I again imagined myself a roboticist, but then I started to pay attention – or to find out, I guess, about the things people like Mark Spong were doing. It didn’t occur to me that control was still an interesting problem for robotics in the early part of the 1990s because I thought you put electricity into a motor and closed a feedback loop and it just worked. I was just completely uninformed about what’s interesting in that world and so in the early mid-nineties, learning from Mark Spong, I, again, realized there’s a lot more out there for robotics than I imagined. I probably had two or three more revolutions in my own way of thinking about robotics before it was all over. I feel at this point that I’ve seen it. I don’t necessarily feel like I know it, but I feel at least I know where the boundaries are. In the 1990s, I came to realize that I didn’t quite know where the boundaries were for the discipline that I had put myself into. 

### 90's Projects

Peter Asaro: 

What were some of the projects that you pursued in the nineties? 

Seth Hutchinson: 

We’ve done a lot of work in my group in planning and that planning in sometimes, “How do you explicitly manage uncertainties in probability theory?” Sometimes the planning is, “How do you develop algorithms that construct essentially feedback control policies?” I consider that to be planning – planning in adversarial situations. The pursuit of agent problem is a problem that a number of my students have worked on. “How do you get robots to maintain line of sight – eyesight contact with evaders that are moving around in complicated environments?” It’s a variation of traditional pursuit of agent problems, but they tend, in that world, not to think about geometric constraints like line of sight, which turned out to be very important in automated systems. 

Peter Asaro: 

What were some of the big challenges in that work? 

Seth Hutchinson: 

The biggest challenge was that the mathematics was really hard and I don’t begin to claim that I really understand the mathematics. I think to do that stuff really well, there are some mathematical tools that you need to understand and there are some computational methods that you need to be able to apply and there’s some hardware aspects that you have to know well enough at least to implement your things on the hardware. And so the mathematics just by itself is already very hard, but to try and learn enough of all of those pieces to push the boundary of the problem that you’re interested in a little bit, I find that to be a big challenge. There’s just a lot of stuff that one needs to know and quite a bit of it is more complicated than I’m comfortable with, so a lot of it, it takes more time for me to learn it than I have time, so that’s the biggest challenge, that robotics is too hard. <laughs> 

Peter Asaro: 

Has that changed over the last few decades? 

Seth Hutchinson: 

Robotics is still too hard. There have been periods, and I suppose many disciplines are like this, when – there have been periods when robotics has not been hard because the mathematics has gotten to a certain level and essentially not stopped, but slowed down quite a lot while hardware implementations caught up. So there’s really no point in doing mathematics three generations out if your hardware is five generations behind because you’re not going to impress roboticists anymore. Leapfrog is the analogy that people tend to use, where the hardware gets to be really good and then people work hard to get mathematical models to describe that hardware and to figure out how to control that hardware and plan to make it do interesting things and then the planning and the control and the algorithms advance to a place that you can’t implement them anymore fast enough to call it a robot system and then that branch sort of slows down for a while, while everybody else catches up. So there have been a number of times when I’ve felt like, “I might catch up now,” but those times never last quite long enough. At the moment, the guys who are doing machine learning are doing sophisticated things. In the time that I started doing artificial intelligence in robotics, machine learning was not at all sophisticated. It seemed to me, it was very much a collection of hacks and clever techniques, without much sound mathematical basis underneath, but today, that’s absolutely not true. They’re using very sophisticated mathematical models and it’s really moving fast and it’s one of the rare times, I think, when the sophistication of the advances in the mathematical side is not outdistancing the hardware side. So these guys are managing to apply their stuff almost contemporaneously to real systems and the two seem to be driving each other in ways that I haven’t seen very many times in the last twenty years and I think it’s very cool, so this is a time when I think everything is moving fast. 

### Funding

Peter Asaro: 

So what are some sources of funding that you’ve had over the years? 

Seth Hutchinson: 

Almost all my funding has been NSF over the years. In the last few years, there’s been a little bit of military money, not a lot, some from ONR, some from the Air Force, but mostly it’s NSF for me. The nice thing about failing to get military funding is that one can take a morally superior tone, but basically I just failed to get military funding for those years. 

Peter Asaro: 

Have you found it difficult to get funding for your research? 

Seth Hutchinson: 

Oh, yeah. I think it’s been a fight. I think everyone – well, most people find it to be a fight to get funding adequate for what they perceive their needs to be and a piece of that is because it genuinely is expensive to do robotics well. You really do need to have nice hardware and you need to have somebody around whose job is to make the nice hardware work and that kind of money is hard to find. The National Science Foundation doesn’t want to hire engineers for you, your university probably doesn’t want to hire engineers for you. Most people that are funding research don’t necessarily want to fund the people at the technical level to make stuff keep happening. And so your smart graduate students are spending some chunk of their time doing technological development that you wish they didn’t have to do, so you wish you had more money to hire more grad students. It’s a resource intensive kind of discipline, I think. Not all disciplines are like that, but I think robotics has that characteristic. 

Peter Asaro: 

We’ve covered a lot of ground. 

Seth Hutchinson: 

I speak quickly. 

### Robotics Failures

Peter Asaro: 

That’s true. So any other specific robots that you would like to mention or that were particularly interesting projects? 

Seth Hutchinson: 

I don’t think so. I mean, to be honest, I have a hard time when someone asks me remembering what I do. I could tell you in twenty minutes, but it takes me a while to sort of sort through, especially at a conference like this, where my brain is in many places. 

Peter Asaro: 

Do you remember any spectacular failures? 

Seth Hutchinson: 

Yeah, but I can’t name them obviously. The spectacular failure are because my style of advising Ph.D. students is not always well matched to the needs of the Ph.D. students. I tend to encourage more autonomy and independence, but then I tend not to follow up and make sure that my students are autonomous and independent and that can lead to spectacular failures, but at the personal level, at the level of individual students not managing to achieve what they wanted to achieve. Yeah, so my biggest regrets are those kind, but I shall not name those people, not that it matters. <laughs> 

Peter Asaro: 

“You’re a robot failure.” 

Seth Hutchinson: 

No, not really. Once I did have a robot grasp an object in such a way that his Plexiglas finger snapped off and flew past the head of the Dean of Engineering, who was there for the demo. I guess that was somewhat spectacular, but not on the scale of giant quadruped robots rolling down mountains. 

Peter Asaro: 

Peter Corke had a mining truck that had a positive feedback loop. 

Seth Hutchinson: 

Yeah, I like to work with robots that can’t – they’re either small enough or fixed enough in place that they can’t track you down and hurt you and Peter’s not constrained by that. His robots can track him down and hurt him, so... 

### Influences and Experiences

Peter Asaro: 

Did you do any sabbaticals at other labs over the years? 

Seth Hutchinson: 

I did. I did a sabbatical in ’97/’98 in Paris at the Ecole Nationale Supèrieure des Télécommunications and I did a half year sabbatical in Rennes with Francois Chaumette, where I learned an incredible amount of stuff. I’m doing a sabbatical now in Rome with the group of Alessandro De Luca where I’m learning stuff about – essentially impedance control and those kinds of things and how to make robots respond rapidly based on forces they experience, particularly in context where humans are sharing their environment. I think that’s it, just those three, and I’ve done a number of small visits to place. I’ve spent a few – a month and a half, I think, in Mexico at some point, a month in Australia at the Australian National University at some point, yeah. 

Peter Asaro: 

Anybody else that you were influenced by in your early career? 

Seth Hutchinson: 

Well, I think I was influenced in my early career by the people that most of my generation were influenced in their early career. There’s a paper by Lozano-Perez , Mason and Taylor called the LMT paper that has enduring influence on how I think about robotics. There was a paper by Rodney Brooks that had a big impact on my Ph.D. thesis, but it wasn’t the behavior based paper, it was the acronym paper, essentially a constraint based system for doing object recognition, which I thought was super cool – propagated symbolic constraints around in ways that I thought was just mind bogglingly cool. The book that Latombe wrote made me understand that I needed to learn a lot more math than I knew and when I met Latombe, he made me understand that I shouldn’t lose the big picture – being lost in the mathematical weeds. And it was very surprising to me that the guy who wrote the book that I found mathematically impenetrable also told me that I shouldn’t get lost in the weeds of the mathematical detail and so that was a point of view that – it took me a long time to understand and appreciate that point of view. So that was a very influential thing and Mark Spong’s work influenced a lot the way I think about robotics probably because the was the guy down the hall doing the coolest stuff, that I could just walk down and talk to at any moment. 

Peter Asaro: 

So in terms of the relationship between motion and vision, were you influenced at any point by the biological theory of vision? 

Seth Hutchinson: 

And by that, you mean how biological systems do vision? 

Peter Asaro: 

<inaudible> 

Seth Hutchinson: 

We read those papers and thought, “These are really interesting,” but they really didn’t affect much, what we were doing. We may have, at times, written paragraphs here and there about, “Such and such is reminiscent of or is analogical to.” Just the highly parallel nature of the brain and the way processing is organized, I never managed to find things that could map directly into the kinds of things that we were trying to do algorithmically, which naturally are – at least at that time and I think even now were serial processing kinds of architectures in very tight control loops. I don’t want to talk much about biological vision because I’m not at all an expert, but the – if you think of biological vision in hierarchical terms, at the top ends of the hierarchy, we didn’t have capabilities, at least computationally, to mimic those in a way that made them useful to understand other than the intellectual curiosity aspect of understanding them and thinking how one day, maybe what I do gets integrated into a bigger architecture that does something, but it didn’t really drive much, the kinds of things that I was doing and thinking about. 

### Evolution and Challenges of Robotics

Peter Asaro: 

What do you think are the biggest problems facing robotics today or the big questions that drive you? 

Seth Hutchinson: 

I think it’s a difficult question to answer. I think some of them obviously are technological actuators and power sources, I think, are holding back robotics in a serious way. There are an awful lot of results in the robotics world today that if you don’t know what’s going on when the cameras are turned off, you imagine robots that can do things over prolonged periods of time, repeatedly. But when you speak to the people doing it, they explain that, “No, it’s fifteen minutes and then we charge the robot for two hours so the batteries can run again.” And it’s the same with actuation. The actuators that are being used are not yet high power, lightweight, resilient kinds of actuators with built-in internal compliance that you really can characterize well and understand well. They’re not yet at the level that you’d want them to be. I think the actuator technology is moving much faster and maybe in five years, we won’t have as many roadblocks from actuators. But I don’t see the power side being solved in the near term and maybe I don’t see it because we’re not doing it. We are relying on another community to develop good power sources that we can then buy and put on our robots down the line. So maybe the battery guys will solve all of those problems, but that is a – it’s a big roadblock. Even the robots that Raibert talked about in his plenary talk yesterday. If you have to put gasoline engines on your robot, there are some hard limitations to what your robots will be able to do, especially in terms of time of operation. So those, I think, are big bottlenecks. The computer vision bottleneck remains and it seems as though the vision side of our world conquers a set of problems and then we do a bunch of cool things, but then another set of problems comes that push it too far. The most conspicuous example of that at the moment I think is that – I think it’s still true that every video that you see of quadrotors flying around doing cool things, those quadrotors are in a room that’s fully instrumented with a sensing system that can exactly measure the position of every quadrotor and none of them have cameras on board, none of them are doing their own vision processing to figure out what their internal state or external state or the neighbors are doing. So I think there’s still plenty of challenge in the sensing side for understanding the world and it’s not just vision, it’s tactile sensing as well. We have tactile sensors now, but they’re really pretty – they tend to be very coarse in their resolution, both spatially and in terms of the disambiguation of forces that apply on them in terms of magnitude. So I think the sensing problem and how does the sensing work to help the robot understand its environment is a big problem that we don’t know how to solve just yet. 

Peter Asaro: 

Do you think the rapid growth of the power of graphics cards and the miniaturization of cameras are helping that? 

Seth Hutchinson: 

Yes. I mean, certainly the camera technology has helped a lot. I mean, for example, having cameras that give you not just RGB, but depth as well, so the whole connect thing has been a minor revolution in robotics sensing because anybody can spend two hundred dollars now and do RGBD and probably do some pretty cool things. But there are some pretty serious limitations on the kind of environments in which those cameras can work effectively. I think the sensing device technology is very good and moving very quickly. The algorithms that can do something with that data, not nearly so much. I think that the GPU technology is super. In the academic world, you don’t get a lot of payoff for taking an algorithm and making it run fast with GPUs. The only payoff you get is if you then have a system that can do something that you can demonstrate real improvement and it’s tough with GPUs to do that because they’re going to be off board somewhere and so now you have some remote processing over there that’s doing all of the work and suddenly it doesn’t feel like autonomous robots anymore. So I feel that GPUs could make a much bigger impact than they have made in part because our motivation as a community is not necessarily super high to exploit them and I think the other part is that our expertise is not well matched because we tend not to be parallel programmers in our backgrounds. We tend to come from the engineering side rather than the computer science side and if we’re coming from the computer science side, it’s typically not the architecture and program and languages side of computer science, it’s the artificial intelligence side, which more and more looks like applied mathematics. If you wander into the machine learning part of the computer science department, it looks as much like an applied math section I think these days as it looks like a computer science department, which maybe is reminiscent of the beginnings of computer science. But there’s been a long period where it’s drifted away from that toward other things and I think we lack the expertise to do parallel implementations in our community. There are certainly some exceptions to that, but not a lot of us are doing that kind of thing. 

Peter Asaro: 

Anything that we missed? 

Seth Hutchinson: 

No, I think you’ve been very thorough. 

### Advice to Young People

Peter Asaro: 

What’s your advice to young people who are thinking about a career in robotics? 

Seth Hutchinson: 

Work really hard, do really good work and really understand the problem that you want to solve before you start hacking and don’t worry too much about the fashion for the problem that you might be working on. Find something that’s genuinely interesting to you and become the world expert in that thing and someone will want to hire the world expert in that thing. That’s also naïve and idealistic and young people shouldn’t probably listen, but it’s what I believe. 

Peter Asaro: 

It’s their job to be naïve and optimistic. Well, thank you very much. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Seth_Hutchinson&oldid=203590 "
