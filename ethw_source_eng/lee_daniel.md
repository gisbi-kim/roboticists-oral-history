1 About Daniel Lee 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Bell Labs 4.3 Early Robotics Projects 4.4 GRASP Lab 4.5 DARPA Robotics Challenge 4.6 Collaborations and Students 4.7 Robotics Conferences 4.8 Machine Learning 4.9 Funding and Sponsorship 4.10 Current and Future Projects 4.11 Approach to Robotics 4.12 Advice to Young People 

## About Daniel Lee

Daniel Lee was born near San Francisco, California. He received a B.A. in Physics from Harvard University in 1990 and a Ph.D. in Condensed Matter Physics from the Massachusetts Institute of Technology (MIT) in 1995. He served six years in the Theoretical Physics and Biological Computation departments at Bell Labs before joining the UPenn faculty as the UPS Foundation Professor of Transportation of Electrical and Systems Engineering in the School of Engineering and Applied Science in 2001. Lee is also the Director of the General Robotics, Automation, Sensing and Perception (GRASP) Lab, a multidisciplinary research center which brings together computer science, electrical engineering, and mechanical engineering for technological development, and co-director of the CMU-Penn University Transporation Center, which focuses on general computational principles in biological systems and development of autonomous systems. 

Lee's research interests in robotics include computational neuroscience models, sensorimotor systems, machine learning, and intelligent robotic systems. His work has earned him several awards and honors, including IEEE Fellow, the Presidential Early Career Award from the NSF in 2004, the 2006 Lindback Award for Distinguished Teaching, and 2008-2011 Evan C. Thompson Term Professor for Distinguished Teaching. 

In this interview, Daniel Lee discusses his career in robotics, focusing on his research at Bell Labs and UPenn’s GRASP Lab. Describing his work on machine learning algorithms and in robotics projects, such as the robot dog and the DARPA Urban Challenge, he comments on the challenges of the field and his research. Reflecting on the evolution of the GRASP Lab and of the field of robotics, he comments on its potential and future. 

## About the Interview

DANIEL LEE: An Interview Conducted by Peter Asaro, IEEE History Center, 16 September 2014. 

Interview #732 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission of the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Daniel Lee, an oral history conducted in 2014 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Daniel Lee 
INTERVIEWER: Peter Asaro 
DATE: 16 September 2014 
PLACE: Chicago, IL 

### Early Life and Education

Q: 

Tell us where you were born and where you grew up and went to school. 

Daniel Lee: 

Sure. My name is Dan Lee. I was born out – near San Francisco, actually the hospital near Stanford University where my dad was a graduate student at the time, and – but soon after that we – at that time we should have <laughs> bought real estate in Silicon Valley and just stayed there, but unfortunately for our finances we moved to northern Michigan where I grew up in the upper peninsula of Michigan until college when I went out east to Cambridge, Massachusetts, where I finished school at Harvard for my undergraduate degrees in physics and then I went for my – actually my physics – I stayed in physics for my Ph.D. at MIT and then I finished there and then moved to Bell Labs. This was at the time it was AT&T Bell Labs and I became a postdoc initially there in New Jersey and I stayed on at Bell Labs for six years as a researcher and then I moved down to the University of Pennsylvania 13 years ago to become a faculty member. 

Q: 

When did the interest in robotics really get started? 

Daniel Lee: 

So the interest initially – I remember reading science-fiction books. I think a lot of robotics researchers remember Isaac Asimov, the science-fiction tales, movies were – in my generation I think “Star Wars” and “Star Trek” kind of shows had just come out, so just to see that in popular media and then thinking about how actually you could create these sentient types of machines was I think a real attraction, but that was kind of just the – kind of a pipe dream at the time. I would say that when I got to MIT and I was studying physics at MIT there was this kind of very big interest groups in robotics. I took a course at the time just – this was the beginning of LEGO robots at the – at that time so really putting together some LEGOs, putting together some microcontrollers and then having little competitions there at MIT. So I remember doing that as a graduate student and but I – that was not my career at that point, I was still a physicist, but when I got to Bell Labs there was quite a number of folks – people from physics, people from biology, from computational neuroscience, and there the question of “What is intelligence in the brain?” came up. And the idea was can we understand collections of neurons as a kind of a system that you could analyze and you could kind of design for and how can we understand intelligence. And then I soon realized that the brain was very complicated, it was very hard to get data from, and so I thought instead of an analytic approach to understanding intelligence a more synthetic approach would be warranted, which then got me into actually starting to think about building robots. And that was – right before then I started to make some robots and then I moved on to the University of Pennsylvania where I joined the GRASP Lab there and started really doing hard-core research in robotics. 

Q: 

What was your physics Ph.D. thesis? 

Daniel Lee: 

So I got my degree in condensed matter physics. It was x-ray and neutron scattering of micro-emulsion systems, which are basically mixtures of oil and water where if you put a little bit of soap in those mixtures they make all sorts of fascinating structures at kind of a nanometer level and you could only use x-rays on neutrons to kind of probe that structure. So the kind of – the draw there was that the existence of these really novel mechanical and dynamical structures that you could only analyze in this kind of indirect way, and in some sense that’s what intelligence is. You have this kind of very complex system, the brain, or trying to understand how perception works or how we do control, and the only way you can analyze that is in this kind of indirect behavioral sense, and to think about then what’s the underlying physics or mechanisms going on inside there at a detailed level is really I think an interesting problem. 

### Bell Labs

Q: 

That was fairly closely related to the work that you did at Bell Labs. 

Daniel Lee: 

Exactly. So there we had a group called Biological Computation where the idea was really thinking about biological systems as computing systems, and that’s obviously a very close connection to thinking about a machine or a mechanical system in terms of computation and trying to have it do control tasks or having it do perceptual tasks. 

Q: 

When did you arrive at Bell Labs and who else was working there? 

Daniel Lee: 

So I joined Bell Labs in 1995. At that time it was still – I became an employee of AT&T. I remember some of the old-timers. There was – at that time there was still a lot of the Nobel laureates who worked there. Arno Penzias was the – still the president of Bell Labs. My lab director also was a Nobel laureate and many, many members of the National Academy of Science. It was really kind of an interesting place where you had people from different backgrounds, from mathematics, computer science, physics, chemistry all coming together. I remember the lunchtimes in the cafeteria where – kind of open discussions; people were playing chess in the mezzanine level there. So yeah, that was in 1995 and I was there until 2001, 6 years. 

Q: 

What was the first project you worked on there? 

Daniel Lee: 

So at Bell Labs actually I constructed a little robot dog at that time and this is before the Sony AIBO came out and using the servomotors, a little – I remember a little video camera for its eye, putting it to a computer system to kind of process the images, being able to control the legs, all the servos, and I remember trying to think about how do walking algorithms work, right; how can you actually get gaits to work on this. And that was the beginning of I guess I would say my full kind of research interest in robotics. 

### Early Robotics Projects

Q: 

Was that the first robot you built? 

Daniel Lee: 

Yes – yeah. Well, at MIT it was a LEGO robot so I guess that I had done a LEGO robot before that but I don’t know – most serious robotics researchers would not count LEGO robots as a first real robot but that was— 

Q: 

Did you have a robotic mentor or were you pretty self-taught in the robotics area? 

Daniel Lee: 

No – so yeah, I basically looked online to see what people had done before and started reading their literature and yeah, so it was kind of – for me it was a self-taught endeavor coming in from a different field, from physics. 

Q: 

What did you do after the robot dog? 

Daniel Lee: 

So yeah, that got me interested in natural algorithms so we were thinking about how the brain – brains or robots can process all this sensory information coming in so I also was doing machine learning. So I crystalized my interest in terms of thinking about how we could implement machine learning algorithms that would help for some of the hard problems in robotics, the kind of hard perception problems, the hard planning problems, the hard control problems, and that basically set my research agenda for the last 13 years now. 

Q: 

What were some of the problems? 

Daniel Lee: 

I think the actual – the main problem is not that you don’t have enough information but you have too much information about the world, right, that the robots are kind of flooded with sensory information, flooded with trying to control so many actuators that you can easily get paralyzed if you are thinking about it at kind of a very detailed microscopic level. So the kind of research that I do is thinking about how we can reduce the amount of information into kind of the relevant dimensions or the kind of – you can think about a dimensionality reduction where we’re kind of simplifying our world view into the relative coordinates that really allow us to make good decisions but then doesn’t paralyze us because we have so much computation to do. So what are the right features to attend to, what are the kind of – the key ways of reducing representations or how do I crystalize dynamical models into something simpler that we can use for planning, right. So these are the hard problems I think that are still with us today in robotics. 

Q: 

What are some examples of the tasks that you got your robots to do in terms of – 

Daniel Lee: 

Sure. So in – on the machine-learning side, one of our first algorithms was to think about recognizing faces or to be able to understand language using some of these algorithms that do this dimensional audio reduction. It also kind of was initially thinking about sparse coding kinds of ideas, which have gotten very big in recent years, and the idea was is there something about again looking at how neurons in the brain represent information; if we can kind of do that same type of representation for robots can they more efficiently say recognize a face or to attend to sounds so be able to localize sounds better or to attend to certain frequencies in terms of discounting echoes in a room environment for acoustic environment. So those are the first initial types of algorithms that I had worked on. 

Q: 

Did you build other robotic platforms at Bell Labs? 

Daniel Lee: 

At Bell Labs the dog was the big one and then I moved to Penn where we got into really big systems where – so yeah, that was kind of the one that I did at Bell Labs and – yeah. Then I had – then I moved to the GRASP Lab at the University of Pennsylvania where then kind of – in the recent years we’ve done so many different types of robots it’s hard to count them now. 

### GRASP Lab

Q: 

What motivated you to move back to academia after industry? 

Daniel Lee: 

I think it was again – well, first of all I could see the writing on the wall for the telecommunications industry so I tell my wife that the best decision I’ve ever made was we cashed out our stock options to buy our house when our firstborn was – when our first son was being born, but you could see that the kind of research environment in kind of the golden age of industrial labs was coming to a close, that they would become much more focused in terms of mandated research and in terms of less freedom to pursue kind of very big questions. So I thought that going to academia at that time would be a good idea so that I could kind of keep that flexible freedom of being able to do curiosity-driven research and to think about large problems but then to have a cadre of students that you could also train that would help you with this type of endeavor. 

Q: 

What were some of the first projects you did when you got to the GRASP Lab? 

Daniel Lee: 

So one of the things I initially got involved with was actually the DARPA Urban Challenge so I thought that was an interesting project. The DARPA Grand Challenge, which is the one that – where they went through the desert, had just recently completed and I saw this as a challenge where we could think about really building a self-driving car and I knew some of the problems in perception and then in planning and control. I could kind of see how you could take a car and kind of hack it a little bit to make it a viable platform that wouldn’t cost extraordinary amounts of money to do this and yeah – so I led the Penn team that successfully completed the DARPA Urban Challenge back in 2007. Oh, another project that I got – I started very quickly with was also RoboCup so I took over the Penn – the University of Pennsylvania had a team. The mentor had just left for industry actually to join a startup so I had taken kind of control and advisory of the RoboCup team, which at that time were playing with little robot dogs to play soccer, and I thought that was kind of a nice platform to try out some of these ideas and to see how students did in terms of learning these systems. 

Q: 

What was the biggest technical challenge that you experienced in the DARPA Urban Challenge? 

Daniel Lee: 

I think the – it was – the biggest technical challenge I think was some of the unexpected things that you would see in the environment. So I remember we had a small team with just a bunch of students. We didn’t have very big corporate sponsors or anything so we had just – we never – we barely tested before we started the challenge so when we took the car I remember we drove it out – we had to bring it out to California for the challenge and the first day I remember this dust storm came through and the LIDARs are basically blinded by this dust. And so out east we never had dust storms so this was kind of interesting, when you go from one environment to another environment the kind of uncertainties of that, how do you deal with that. And so we ended up thinking about kind of better ways of making sure our – the signal processing was robust enough that these – this kind of scattering that you got from the dust clouds would not affect the actual performance of the car, but I remember thinking wow, this is a real-world thing, that – they had eliminated rain, they said that we didn’t have to worry about rain, but just even a dust cloud was giving us problems. So I remember thinking at that time that robotics is still not really ready for prime time just because you move a car from one environment to another, a robot from one scenario that you trained on to another scenario, still was very difficult for it to kind of on its own be able to respond correctly. 

Q: 

In the RoboCup did you find more challenging the perceptual issues or the coordination issues or – 

Daniel Lee: 

So I would say recently at RoboCup we’ve gone to humanoid soccer and that’s made it a very interesting problem because with bipedal locomotion the stability issues become very key, right, in terms of we still don’t understand very well how humans do if your friend comes and – <break in tape> how well we actually do the control and managing our vestibular system and being able to respond to that, being able to decide when to put my – when – if I have to move my foot over here or if I should swing my arms in this direction. All these things that we take for granted in terms of balance and stability for using our two legs we have – I think we’re still just scratching the surface in terms of what we can do with the robots at this point so that’s why you see these robots like ASIMO, right – I mean the walk – it will only walk very well on flat ground and it looks very slow, cumbersome. We’re only starting to think about really make them robust for rugged terrain and for running and researchers are doing a lot of things toward this – towards that goal but we’re still far away from that. 

Q: 

Do you think you’ll be able to beat the RoboCup team – 

Daniel Lee: 

<laughs> So that’s a good question and it’s hard to predict the future, right. I mean seeing as I said some of these problems, these kind of serious problems, I think we still don’t have that great of a clue in terms of how to approach those problems, you would say, “Well, no way, it’s going to be impossible to have a robot that’s going to run around and jump and be able to sense things in sunlight environments where you could have shadows and all sorts of things like that,” but 30, 40 years is a long time, right. If I – that’s – I guess looking back to when I was a little child, no one would have predicted cell phones or the gadgets that we take for granted or how far computation has advanced so now – in terms of how well we do algorithms for the web. So 40 – 30, 40 years we might have some breakthroughs that really advance this field. So yeah, it’s – I don’t know for sure. I would say no but it’s hard to see exactly what will happen in that long of a time. 

### DARPA Robotics Challenge

Q: 

What are some other robots you’ve worked on? 

Daniel Lee: 

So – yeah – so more recently we’ve also had a group working on this DARPA Robotics Challenge so we’ve been collaborating with other – with Dennis Hong’s group and a Korean company where they’ve done the hardware design for a big bipedal humanoid that will do a search and rescue, but my students have been handling kind of again more on the intelligence side of things, again how to do perception, three-dimensional, being able to do a localization and doing – servoing towards manipulation types of control, and then the planning, how do you the trajectories, how do you do the walking algorithms. These are again the things that we’ve looked at in the past but now it’s gotten more complicated; you’re trying to do everything at once where you have manipulation and locomotion together. So I think these large bipedal humanoids have been kind of interesting to see how well – how close we can get to an approximation of some of the human-like capabilities that people are looking for. 

Q: 

What’s the creating company – 

Daniel Lee: 

This creating company is called Robotics. They actually make these modular motor – motors that are – recently in the last year they’ve essentially come out with very high-torque compact modules and building now a large-scale robot like this humanoid robot is a little bit like building a LEGO robot; you just plug these things together. And the problem now is really the software behind it, the control. 

### Collaborations and Students

Q: 

You have an affiliation with KAIST in Korea. Do other collaborations with Korea? 

Daniel Lee: 

So yeah, we have a number of projects where we have friends and colleagues in the different universities and research institutes there so it’s always interesting because between the U.S. and East Asia you see these kind of cultural differences in how people on the street approach robots. One thing I would like to say is when you mention a robot to a person here in the U.S., right, they’ll think of Terminator whereas if you go to Japan or Korea and they’re thinking Atom Boy or something. So you see this kind of – very much robots are here to help us or robots are here to take over the world mentality and there’s – there definitely is an East-West divide. So kind of the funding and the kind of – the kinds of problems that the governments and the research institutes in East Asia are approaching are different than what you see here in the U.S. And so I think having seen both sides it’s actually kind of an interesting thing to do. 

Q: 

Do you see their investments catching up with the Japanese investments? 

Daniel Lee: 

No – Definitely, yeah, I think you’ll see in the next few years that China, Korea, Japan, all these countries feel like being able to automate and to put a little bit more intelligence into machines is definitely the future economy. 

Q: 

Other collaborations outside of U Penn have been important – 

Daniel Lee: 

So – yeah, I mean at Penn I’m filling in with the GRASP Lab and I’ve been directing it for the last couple years and so we have a number of big projects where – there’s a robotics consortium that we’re involved with that’s Carnegie Mellon. I also direct the University Transportation Center, which is also a collaborative center for the Department of Transportation thinking about things like self-driving cars now in real life so – and that’s again a collaboration with Carnegie Mellon. And we’ve had joint projects with all the different big players in the U.S., Stanford, MIT, Georgia Tech, Cal Tech, all these so it’s nice. There really is a sense of a robotics community both domestically as well as internationally and so depending upon the projects you can kind of get resources or ideas from partners across the world. 

Q: 

Who was at the GRASP Lab when you started and how has it evolved and how did you wind up as the director? 

Daniel Lee: 

Sure. So when I first got to GRASP Ruzena Bajcsy had just stepped down as director. She was heading to the National Science Foundation as – to head the directorate there and then Vijay Kumar had just taken over as director of GRASP. So it was kind of a nice environment to see these big giants in robotics and I was just a fresh assistant professor at the time and to see kind of how centers like this were kind of organized and use the – kind of be able – you want these centers to be more than the sum of their parts and I definitely think GRASP was a good example of that where you had people – as I said with robotics being so broad you had people coming in from computer vision, you had people coming in from controls, you had people coming in from – myself – from machine learning thinking about how all these different aspects could be put together to design a single system, which is definitely more than the sum of its parts. And in that sense GRASP Lab was something that I saw as a place where you could see that happening and I learned a lot just by being a member of it. And so – yeah – so Vijay was director for a while and then George Pappas who is in hybrid controls took over and that was again a nice transition to – going from we had someone from computer science, we had someone from mechanical engineering, now George was coming from electrical engineering, and Kostas Daniilidis was more – was also then the director, and then two years ago he became associate dean and I – they kind of twisted my arm to make sure that I could become director so – I never thought I would be doing administration because if you like your research so much you always say you never want to do this but I felt like this was a good – to be able to make sure that say the next generation of students and faculty would also be able to benefit so— 

Q: 

Who were some of the Ph.D.’s you supervised who have gone on to do work – 

Daniel Lee: 

Sure. Yeah. I mean I’m proud of all my Ph.D. students. My first Ph.D. student is now actually a director at NEC Research Labs in California where he runs a big group on thinking about machine learning, vision systems, implementing these for real-world types of applications using resources from the web, kind of big data types of projects so he’s done very well and we – It’s always nice to be able to sit down and see your old students at conferences and to go and have dinner with them and find out how their kids are doing now and you knew them before they were married and just to see kind of the growth in their lives and – both on a professional level as well as on a human level. 

Q: 

What was his name? 

Daniel Lee: 

Yuanqin Lin, L-I-N. 

Q: 

Any others you want to – 

Daniel Lee: 

Sure. Jihun – so I – he was – Yuanqin was a Chinese student of mine. Jihun Hamm is now at a research faculty, Ohio State University. He actually went more in the – he did some machine-learning robotics projects but he’s gotten more into the biomedical area so he’s doing research there. Yeah. So again I’ve seen him at some conferences recently as well and so those are my – so I’ve been there 13 years so they graduated 7 years ago now so this is kind of my first batch of Ph.D. students so hopefully in another 10 years down the road I’ll have – I’ll be able to – hopefully be able to name all the different ones that have come out but these – those were the first two that came out of my lab. 

### Robotics Conferences

Q: 

When did you really start going to robotics conferences or the IEEE in terms of your career development? 

Daniel Lee: 

So yeah, that – I would say – so I started robotics research at Penn 13 years ago and then I realized okay, I should start getting more involved with the actual societies and the conferences so we started submitting our – probably our first papers 10 years ago and so – and that’s steadily built up where I’ve gotten more involved with the organizational committees and things like that in the last five years. So it’s been – coming from a different field where you don’t – you haven’t been say a Ph.D. student in the area it’s kind of different. It’s – you have to kind of figure out the landscape of the actual field, who – what the kind of various groups are doing, who are kind of the nominee – the figureheads around that you should definitely know their work and keep track of. So it’s interesting to see kind of – and especially in robotics. It’s as I said so broad in terms of its scope and also internationally where you have pockets of concentration in the U.S. and Europe and Asia just to try to get that feel for what people are doing and what interests are going where. So that’s taken me a while but now – I think now with IEEE and with these kinds of conferences like ICRA and IROS you can see kind of a snapshot of this whole process going on. 

Q: 

Are you still an active member of the machine-learning communities and AAAI and these kinds of conferences? 

Daniel Lee: 

Sure. Yeah. So in the machine learning in the NIPS conference, ICML, I send students to almost every year, AAAI, so – yeah – so I keep involved with – on the machine-learning side with those conferences and groups as well as trying to keep my robotics affiliations, but it gets hard to do because there’s now so many conferences that – and they’ve gotten so big and the interest I think recently where people have seen this is really a growth area some of these conferences have now exploded in terms of numbers of attendees so it’s interesting to see the evolution of this. 

### Machine Learning

Q: 

What do you think the biggest breakthroughs in machine learning have been over the last couple of decades? 

Daniel Lee: 

I think definitely that the amount of data that you can process has really, really scaled up, and I don’t know if that’s a natural technological breakthrough or more of – because of Google, Facebook and Amazon getting involved with this process. And I think just seeing the scale now of these experiments people do is mind boggling, how much data that they can put through an algorithm and then be able to have it process billions of images and then to be able to extract something out of that. And maybe that’s the way we – there’s been a recent push in cloud robotics and maybe that’s the way we do this, right. We really try to leverage what’s out there on the web and what’s out there in – on the Internet to enable our robots to do more capabilities. I still think that we haven’t really gotten the secret of the right representations or how the brain does this kind of intuition, right, so I still think that what’s lacking is a science of intuition for the brain, right, when we play chess that we are not calculating every single move, we have some intuitive sense of this is the right way to think about it, or when we do a task we have some intuition that maybe I should try this rather than trying all possibilities. So this is still I think a key area where we don’t know how to make a machine have that kind of natural intuition to do a certain task and that – that’s still I think the big research challenge that my group is working towards. 

Q: 

Do you see deep learning as a form of mass data – 

Daniel Lee: 

It is. I mean it’s a nice way to basically build a model of data by putting together a lot of neurons in lots of layers and having hopefully an efficient training – learning algorithm that will be able to tune up all these parameters so it’s – you can’t argue with its successes in terms of the classification rates that it’s getting to but there still is lacking a little bit of – and people who do this will tell you that the science of understanding this process, right, the – what’s special about that representation or what’s special about their learning role or the way they are dropping out their data to do their learning. So there’s still a lack of kind of theoretical understanding of their results. 

Q: 

Computational learning theory is trying to shore up some of the theoretical foundations for that. 

Daniel Lee: 

Yeah, but I think you are – you’re still lacking kind of the understanding of exactly what the learning curves are going to be like for a particular situation, the bounds that you get are not very tight in most situations for the theoretical – between the theoretical bounds and the actual practice of it there’s still a big gap. And so kind of – people right now are just putting things out there and trying it out and seeing what works best without really this kind of deep understanding of what’s actually going on inside their computers so it – it’s still the wild, wild West in that regard. 

Q: 

Machine learning still has a lot to offer to robotics? 

Daniel Lee: 

I think so. I mean the problem with the approaches that we talked about is that robots have this kind of very hard real-time constraint and they break if they do something wrong so it’s not like where you can have an algorithm and try something a billion times to see what works well. A robot – eventually you might want them just to go into a new environment and within a few seconds be able to adapt to it and to generalize, and again I think that requires some sense of this intuition that something I did before I have to kind of change it a little bit so that it’ll work well in this environment without having to try every single possibility, right. So this is – I think this is still key for robots and I think we don’t – and on the machine-learning side we don’t understand that, what is the right feature – what’s the right representation, what’s the right way of reasoning about these situations that can generalize to new situations very easily. 

Q: 

Do you have a plan on how to solve this problem? 

Daniel Lee: 

No. If I knew I would be doing it but I think we’re making baby steps and it’s an ongoing – and that’s what research is, right, that maybe someone in India will come up with a good idea and someone in Europe will then try it out and show it actually works in this domain and then we hear about it in a conference. And then we can then try it out in different situations and then maybe someone comes up with a theoretical kind of model for it that then makes sense and then that gives new ideas for generalizing these kinds of algorithms. I think that’s the way science should be working. 

### Funding and Sponsorship

Q: 

Where have you gotten most of your research funding over the years? 

Daniel Lee: 

So almost every agency that you can get research funding from so obviously in the U.S. the National Science Foundation, the Defense Department through the navy or the army or through the air force or through DARPA; those are the big kind of funding sources for robots. We’ve gotten private so industrial funding from Intel, from Microsoft, from different foundations, from companies, Lockheed, Northrop Grumman; these kinds of companies have donated and then also some private contributions from some of our alumni. That’s the nice thing about showing these robots sometimes; you get some people – when I give some talks for alumni they – a lot of them get inspired and they say oh, they want to help out with sponsoring students and things like that. So you can see that robotics really touches a nerve with a lot of people, just the potential game-changing aspects of its capabilities. I think people understand that whether it’s kind of a science-fiction understanding of it but they can see that and it’s quite easy to kind of convince people this is a worthwhile endeavor. 

Q: 

Have you had other more direct collaborations with companies? 

Daniel Lee: 

In some sense, yeah. They have sponsored projects usually as an academic partner. We usually have them give us a gift or they’ll be a partner as a co-PI on a project so yeah, we’ve had direct kinds of things with some of these companies that I mentioned, Lockheed or the – yeah. 

Q: 

Have you been involved in any startups? 

Daniel Lee: 

Myself, no. <laughs> So I tell my wife unfortunately I have the anti-Midas touch so if I actually went into some business endeavor I probably would do the opposite effect and probably ruin it so no. I mean I’m happy with research and I’m comfortable enough with the kind of salary that you can get from teaching and from research and so I don’t need to make the big bucks for a startup or anything like that. 

### Current and Future Projects

Q: 

What projects are you working on now or looking forward to in the coming years? 

Daniel Lee: 

More recently, I’ve gotten – I’ve gone back and tried to think about computational neuroscience so is there something actually we learn from some of the algorithms that we’re doing so say some of these probabilistic models that we’re using in robotics these days; does that actually occur in the brain. So I’ve had some students and some colleagues that were thinking about what are the implications of some of these algorithms in terms of what neurons might be doing, and so it’s been interesting to think what’s now known about how the brain works, some of the new imaging technologies that have come along. I would have never thought when I – 15 years – 13, 15 years ago that we’d be able to start to measure multiple units of neurons as a person is doing a task, right, but now we are – you’re – you can kind of see that now might start to be possible. So do we have some – can we take some of the models that we use and say, “This is how you get a machine to do it; is the brain doing the same thing for us?” I think it’s now maybe time to start thinking about closing that – closing the loop on that. 

Q: 

Are you looking at some of these big brain-modeling projects with IBM – 

Daniel Lee: 

Sure. Yes. Yeah. So I have a number of colleagues who are involved with these – those big projects and it’s interesting to see their approach, right. I mean is it build it and it will come or is it you need to collect all the biological experiments and throw it together and something will emerge out of that process or you build first a big simulation and somehow just putting everything together it will be self-organized, some sort of symbiosis of this. And that’s some of these ideas, right, of how the brain might work, and again I think there should be a little bit more of a – kind of a harder theory of this, which is lacking. 

Q: 

In your role at the transportation center, what are the big issues coming up with self-driving cars and where do you see that – 

Daniel Lee: 

Sure. So for self – I mean it’s amazing to think that coming from the DARPA challenges, which were just seven, eight years ago, that we’re now having companies that are really seriously thinking about rolling out products with these technologies. I mean the kind of time from basic research to actually something that will change many people’s lives is incredibly short. That’s – I think that’s a very big success story for robotics and you can thank some of the pioneers like Sebastian Thrun and – for pushing that vision ahead. Obviously, they – once you get to that level, the – how – the dirty secrets like none of these things will work in the rain still, right, and so there’s still technological issues there, but I – and then in terms of implementation, right, how do you handle the liability issues. I mean these are – how do you – what does policy have to do with – government policy will then encourage or discourage use of these types of technologies, when you have the first couple accidents how people will respond in terms of will they shut down the whole process. I mean these are I think some of the key questions and so the idea is what are kind of the low-hanging technologies that one should really leverage and start putting into things that might help with transit systems or might help with car sharing, right. I mean you can imagine many scenarios where some of these technologies would really be very valuable. 

### Approach to Robotics

Q: 

Is there anything we haven’t covered? 

Daniel Lee: 

Oh. <laughs> I don’t know. Are you trying to get a lot of sense of what people’s approach to robotics is or do you kind of – 

Q: 

Yeah, and also changing over your career and you’ve come into it obviously and where it’s heading. 

Daniel Lee: 

Yeah. I mean I guess from – as a – when I started in robotics as an outsider perspective I thought of it as kind of – very much a – it seemed more like a mishmash of people doing things and it wasn’t as unified as say coming from the physics community where you really had kind of basic canons that everyone subscribed to so people working in particle physics were at that time going after the Higgs boson, that was the thing to do, right, whereas people in – working at the larger scale were looking for black holes and nebulae and things like that. The question in robotics is what is that kind of big problem that we’re going after, right, what is the big – so that’s what the DARPA Grand Challenges have been, right, let’s define an actual task where if you get a robot to do that’s the grand challenge that we’re looking at, but the question is then what’s the scientific question behind all this. And for me it’s really how do you get a robot to truly understand in some sense its environment, right; what is its model in the environment; how does it learn. These are the questions that I think are still the deep scientific questions. It’d be nice to be able to kind of maybe think about robotics not as kind of an application of a – to do a certain task but to think about again more the fundamental science behind it. And I think there’s some other researchers who are thinking along those lines or what’s the fundamental scientific advances that need to be done and then we can also then do the implementations in systems, but I think that – it would be interesting to see if those questions can be more fully articulated in the next few years. 

Q: 

It would seem that a big part of that is also the systems integration piece of it. 

Daniel Lee: 

Yeah. Now having done that, obviously systems integration is very important and how to do that properly is key to get successful systems, and when you go to conferences you see people more on the application system side and people who are thinking theoretical but then kind of bridging all that together has been sometimes very difficult to do. So maybe there’s more of a mechanism where we can kind of encourage that where we have real scientific advances but then being able to put those into real systems in kind of a more transparent way. 

Q: 

What was the big challenge in the DARPA Rescue Challenge technically speaking? 

Daniel Lee: 

Yeah. So the challenge for me – you mean from a scientific perspective? Well, first there was a big systems challenge, just getting the thing so that if it falls once it’s not going to just fall to pieces, right, just – or your cables will all pop out or your battery will not be able to power the thing after ten minutes, right. So these are all the kinds of nitty-gritty stuff that you have to get right, but for me it’s kind of a question of being able to – say manipulation and locomotion simultaneously where you have uncertainties in both, how do you then kind of reason about that properly so that you can actually – how do – for us how do we actually learn how I use my hands versus how I use my feet and using them simultaneously. It’s not like a kid who first learns to walk first and then stops and then learns to manipulate things with his hands; they’re kind of doing it all together. And for us in robotics we’ve separated the two, right. We’ve had people working on locomotion, we’ve had people working on manipulation, and now with this challenge they’re just kind of in some sense hacking it together, putting it together, and maybe that’s not the way we should be thinking about it; it should be more of a holistic type of understanding of interactions with a three-dimensional environment. So these are some of the challenges and scientific questions I think would be interesting to see if they do get addressed in the next few years. 

### Advice to Young People

Q: 

What’s your advice to young people who are interested in a career in robotics? 

Daniel Lee: 

Yeah. I’ve had a number of kids when I’ve given these talks and – come up to me and they want to get involved with robotics and I think that’s great, right. This is something you can see, you can get your hands on, but again there is some fundamental things that you need to learn first these days, knowing obviously linear algebra; knowing probability theory; being able to think about how – the mathematics of reasoning, the mathematics of decision making as process models; how our physical interactions work, right; what is the nature of friction, right. I mean before you can make a robot that really can do manipulation well the designer has to know about what the physical properties imply about control and manipulation. So kids love robots, they come up and – but I would still say, “Look. The fundamental math and science behind it you – I think you have to really get that basic grounding first and that – so before moving to something that seems sexy and doing that I think you need to kind of go through this process where you understand the basic science behind physical interactions, behind the mathematics of models, right, the kind of probabilistic nature of uncertainty, right. These are all things that have to really be put into the robots. 

Q: 

Great. Anything else you’d like to add? 

Daniel Lee: 

That’s it for now so – 

Q: 

Thank you very much. 

Daniel Lee: 

All right. Thanks. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Daniel_Lee&oldid=182330 "
