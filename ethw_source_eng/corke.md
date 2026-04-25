1 Peter Corke 2 About the Interview 3 Copyright Statement 4 Interview 4.1 Early Life and Education 4.2 Working for CSIRO while pursuing a Ph.D. 4.3 First Robot 4.4 Mining Robotics Work for CSIRO 4.5 Sensor Networks 4.6 Collaborations 4.7 Professor at Queensland University 4.8 IEEE Robotics and Automation Society 4.9 Ph.D. Students 4.10 Robotics Experiences 4.11 Advice to Young People 4.12 Future Challenges 

## Peter Corke

Peter Corke was born in Melbourne, Australia on August 24th, 1959. He attended the University of Melbourne, where he earned his bachelor's and master's in Electrical Engineering in 1980 and 1986, respectively. Following graduation, he joined the Australian government research agency, CSIRO (Commonwealth Scientific and Industrial Research Organization). While there he pursued and completed his Ph.D. at Melbourne. He continued at CSIRO where he remained until 2008, after which he wrote a book on visual control networks and then joined the Faculty at Queensland University of Technology as Professor of Robotics and Control, a position he holds today. Corke has worked himself in several aspects of robotics, researching mining and field robotics, control theory, computer vision systems, and wireless sensor networks. He served editor-in-chief of the IEEE Robotics & Automation Society (RAS) Magazine from 2010-2013. 

In this interview, Corke discusses his career in the field of robotics. He recounts his research work during his college and graduate years, at CSIRO, and at Queensland University. He discusses his contributions to the field, particularly his visual control textbook, his work on mining and field robots, and on sensor networks, his research in visual servoing, and his contribution to the development of open source toolboxes. Additionally, he provides advice to young people interested in robotics, and reflects on his many collaborations, and the challenges and future of the field. 

## About the Interview

PETER CORKE: An Interview Conducted by Peter Asaro, IEEE History Center, 4 November 2013. 

Interview #694 for Indiana University and IEEE History Center, The Institute of Electrical and Electronics Engineers, Inc. 

## Copyright Statement

This manuscript is being made available for research purposes only. All literary rights in the manuscript, including the right to publish, are reserved to Indiana University and to the IEEE History Center. No part of the manuscript may be quoted for publication without the written permission the Director of IEEE History Center. 

Request for permission to quote for publication should be addressed to the IEEE History Center Oral History Program, IEEE History Center, 445 Hoes Lane, Piscataway, NJ 08854 USA or [email]. It should include identification of the specific passages to be quoted, anticipated use of the passages, and identification of the user. Inquiries concerning the original video recording should be sent to Professor Selma Sabanovic, [email]. 

It is recommended that this oral history be cited as follows: 

Peter Corke, an oral history conducted in 2013 by Peter Asaro, Indiana University, Bloomington Indiana, for Indiana University and the IEEE. 

## Interview

INTERVIEWEE: Peter Corke 
INTERVIEWER: Peter Asaro 
DATE: 4 November 2013 
PLACE: Tokyo, Japan 

### Early Life and Education

Q: 

Just tell me where you were born and where you grew up and went to school. 

Peter Corke: 

Sure. So I was born in Melbourne, in Australia, and went to school initially in Melbourne. Then, moved to the countryside, a little town called Castlemaine, which is where I went through high school, and then, when it came time for university, I went back to Melbourne and went to university there, studied electrical engineering and did a Master's degree, as well. 

Q: 

And did you sort of always know you were going to do electrical engineering? Or how did you-? 

Peter Corke: 

Absolutely, I think from quite a young age, I knew I was going to do something with electronics. I built radios, pulled television sets apart, things like that, when I was a kid. So yeah, it was pretty clear I was going to be an engineer, and probably an electrical engineer, and yeah, I guess, when I was at university I got interested in computers and digital systems. 

Q: 

What was your master's thesis? 

Peter Corke: 

So my master's thesis was in the area of control theory. So that's the particular discipline that says, "Okay. You've got a machine that's got some dynamic characteristics and it behaves like this, but I want it to behave like something else." The control system uses feedback theory to make it do what it is you want it to do. So it's one of the elements of robotics. So yeah, after – I was interested in that as an undergraduate and at the end of my study, didn't really have a job so I hit up one of my professors, and he took me on as a research assistant, and so I did that. I was there for three years, did my Master's during that time. I was a research assistant for one year and then he got some money to buy himself out of teaching. So that bought me into teaching. <laughs> So for the last two of those three years, I was teaching at the University. So I taught digital systems and control theory. 

### Working for CSIRO while pursuing a Ph.D.

Q: 

And did you stay there for your Ph.D. or did you move out of there? 

Peter Corke: 

So at that – after I finished there, I went and worked for a government research agency, an organization in Australia called CSIRO, Commonwealth Scientific and Industrial Research Organization. So it's an applied R&D organization, and so I was with them for a few years before I did my Ph.D.. So they kind of sponsored me to do my Ph.D., so I did that part time over three and a bit years. It was kind of aligned with my day job, which is kind of brilliant. You get paid to do your Ph.D. and it's aligned with your day job, so it was about as good as it could get. 

Q: 

Who was your dissertation advisor? 

Peter Corke: 

So my advisor was a Professor at Melbourne Uni called Malcolm Good. He'd been at Melbourne University for quite a while. He spent a period –I think he was on sabbatical –at the GE Research Labs in Schenectady, and he worked there with people like Mark Spong on manipulated dynamics. And when he came back from his sabbatical, he actually joined CSIRO for a while. So at CSIRO he was my boss, and then he went back to the university, and I then became his student, like, about a year later. The other thing that's interesting around this time was that I spent a year in the US. So I'd done my master's. I was working for this organization, CSIRO. I started with them in '84, and in '88 I won a fellowship that let me go to the University of Pennsylvania to the GRASP lab, which is still a powerhouse of robotics research. So when I was there, Lou Paul was there, Ruzena Bajcsy , Vijay Kumar was there. I was working, particularly, with Lou Paul. He was the guy who hosted me there, and I spent nine months at the GRASP lab, and it was brilliant, and it was at that point I'd sort of finished with the GRASP lab, I came back home and think, "Yeah, I want to do a Ph.D.." And then, management said, "Yeah, that's fine." 

Q: 

And what was your dissertation work on? 

Peter Corke: 

So my dissertation was on vision-based control. So how do you control what a robot does using images that come from a camera? Which is, either watching the robot or which is on the end of the robot, watching what it's doing. Before I went to Pennsylvania, I was involved in a project, where we're developing some special purpose hardware for processing images from cameras quickly. This is a long time ago. This is in the 1980s. Computers were really slow, and they couldn't process images very quickly. So we built this amazing hardware system that images from a camera would stream through this thing, and what would come out is what we call blob features that would tell you where the objects were in the scene, how big they were, what their position was, and whatever. And you needed a special gadget like that if you were able to take data from the camera, like 25 frames per second, get it into a fairly concise form, which a robot could act on, and if you've just got millions of pixels spewing out of a camera, in those days that was too much for the computer to deal with. But with this special board; right, which would reduce the data rate, give you just the essence of the image then, yeah, that could go into a robot. So I worked on that project and that hardware was used in all sorts of things. It was used for food processing and traffic monitoring. I took one of them in my bag when I went to University of Pennsylvania, and so there I kind of built my first vision guided robot system, and it worked and that was nice, but performance was not as good as it could be. So my dissertation was really doing some very detailed modeling of the dynamics of a camera, this image processing system, and the robot, as a complete system. And once I had a decent model, then I could design a control, which would really allow a thing to move very, very quickly. 

Q: 

Were you looking at manipulators at that point for the robot end? 

Peter Corke: 

Yeah, so I had a robot in my lab, one of the Unimate PUMAs, or PUMAs, as Americans call them, and that was my lab rat, and I did all my work on that. And at the time, '80s, early '90s, the Puma was the workhorse of robotics research, and they're all in rubbish bins now, and people use other kinds of robots. But at the time, that was the machine. 

Q: 

Some of them are in museums. 

Peter Corke: 

Yeah, a couple of them are in a museum, the rest in rubbish skips. <laughs> 

### First Robot

Q: 

So what was your first robot? Was that your first real robot? 

Peter Corke: 

The first robot that I had anything to do with was when I was still at the University of Melbourne, and I can't remember why we did this, but I bought a really early, sort of, toy robot. So it was a little robot arm. It probably had a reach of this – like, five stepping motors or something like that and I wrote a program to make it play checkers; a draft, as we would call it. And so it played on a board about this kind of dimension, and I connected it up to a mini computer. So your mini computer's like a rack of equipment like this. So I connected the little robot up to that and made the individual joints move, and then put in an algorithm to allow it to play checkers, and I remember for an open day, we had it set up so visitors to the university, they could make their move. I think I had to type into the computer what their move was and the robot would come and move its own piece, and the person would move their – that was pretty successful as an open day demo, and that was really my first experience with a robot. 

Q: 

Okay. I'm just going to pause for a second. 

### Mining Robotics Work for CSIRO

Q: 

We're back on. So how did you finish your Ph.D.? Did you go back to CSIRO? 

Peter Corke: 

Yeah, I did, because, I mean, I was still technically working for them. That was my day job. So I stayed there for a while, and the day job was in a few different areas that we were looking at the application of this high-speed computer vision technology, and we did a food sorting machine. We did a big traffic monitoring system, which is actually still running in Australia, and we'd also done a bit of work in the manufacturing sector, and manufacturing in Australia has always been a big fraught. We still just have a manufacturing industry, but every year it gets less and less, and it was problematic even back then in the '90s. And so we work with some indigenous robot manufacturers and machine tool manufacturers trying to upskill them. That was probably, long-term, a losing proposition. So one day, the chief of my division said, "How would you like to move to Brisbane and get involved in mining robotics?" Just manufacturing robotics, mining robotics, how different can it be? So talked about that with my wife, and eventually, we decided yeah, we'd do that. So I moved to Brisbane in '95, and started a small activity in mining automation and mining robotics. 

Q: 

So what was the scope of industrial robotics in Australia? Was it pretty much focused on mining and manufacturing? Or were there some other companies? And how would you compare it to the US or Japan? 

Peter Corke: 

I think – the fundamental different, I think, between, say, the US and Japan is that Australia doesn't have a very – we've got a small population, and we're a relatively small manufacturing industry, and to service just the local population, it's not really – it's not really cost effective. And the country used to be protected by tariff barriers, but traffic barriers started to be torn down in the '80s and '90s, and the local manufacturers just couldn't compete with imports. So Australia was, at one time, probably quite self-sufficient in manufacturing everything. The textile industry died; shoes, footwear died; car industry started a long decline, which is almost played out now. So in some ways it didn't make sense to do manufacturing robotics in Australia. It just didn't fit with the economic foundations of the country, and Australia's interesting in that it's considered to be a first world country, but the economic underpinnings are really that of a third world country. I mean, it's based on agriculture and mineral and energy exports. That's what keeps the country afloat. So it was – what happened in the '80s and '90s is – and to think, "Well, okay. In Japan, they have particular applications for robotics in manufacturing. In Europe, also, they do manufacturing. The US, yeah, a lot of manufacturing and some military staff. Japan and America had nuclear reactors and things that needed cleaning up, so then, the robots for those applications. None of those things made any sense in Australia. I think, for a while, we just were slavishly following what everyone else was doing. I think in the '90s, though, the penny dropped and it was that we should do robotics that made sense in Australia. So the sort of two groups, quite strong groups, grew up in the '90s. The group at CSIRO, where I was, we pushed into mining robotics, and there was the group at the University of Sydney, so Hugh Durrant-Whyte group in the Australian Center for Field Robotics, and they did work in mining area, as well, and they also did a lot of work in logistics and container port automation and the like. So I think both groups realized that if you want to do robotics in Australia, you had to go after something that was economically important. And after working with, say, the manufacturing industry, which was really – it wasn't very healthy. A lot of very small companies weren't well capitalized, weren't really able to invest in robotics research, probably weren't even able to invest in robots that you could just buy off the shelf. Mining, everything was completely different; huge turnover, and if you used robots to improve the productivity of a process like digging the dirt that uncovers a coal seam, improve that productivity by, say, a percent, to the company, it's worth millions of dollars a year. It would pay for itself in less than a year, and so just the numbers worked really well in mining, where they didn't work very well in manufacturing. So there was kind of a push factor and there was also a pull factor. Mining also has a safety consideration, as well. A number of miners are killed and injured every year, and that number's much, much less than it ever used to be, but it's not zero. It's plateauing out at some number bigger than zero, and it will be that way while there's human beings involved in the process. So the early big dream for the mining guys was to no people underground or in dangerous places. We just put machines there, and that way, then, you'll get the perfect safety record. 

Q: 

What would you say were the big robotics issues or questions or problems that you started addressing when you moved into mining robotics and field robotics? 

Peter Corke: 

So the biggest challenges in mining automation is that the world is continually changing. That's the process of mining; right? <laughs> You start with a nice pristine environment and you want to transform it so you can get the minerals out, so everything is changing continuously. Where the paradigm in manufacturing is everything's static and arranged beautifully. The robot knows where it is. The robot knows where all its work pieces are. It knows that if it reaches to this coordinate, it's going to get the object that it wants and it's going to put it over here at this coordinate. So very coordinate oriented, and underpinning assumption that the world is time invariant. In mining it's not like that. You don't exactly know where the machine is. You don't exactly know where is the thing that it needs to manipulate, yet it needs to do that. And what was interesting about that situation is it actually uses some of the ideas that my dissertation was about. So if a robot's got a camera in it, for example, and it wants to reach the widget, it doesn't need to know where it is. It doesn't need to know where the widget is. It just needs to be able to move so that the distance between the hand and the widget goes to zero, and so those ideas about the relative positioning become important in environments, which are unorganized and continually changing. 

Q: 

And how long did you stay at the-? 

Peter Corke: 

So we started in '95, and it was just two of us, and we grew that activity over a period of years, to a lab with 40 people in it in 2008, which was when I finished at CSIRO. So certainly, the period between '95 and 2005, we did a lot of work in this mining automation area. So we automated massive excavating machines, machines that weigh 3000- 4000 tons, and are used to uncover coal seams. We automated machines that drive in the underground tunnel networks of metal mines or copper mines, gold mines, those sorts of things, and, certainly, that technology in particular was licensed to Caterpillar, and that's available as a product they sell called MINEGEM. That was an underground vehicle navigation system, and that was probably – that was kind of the peak time for the mining automation work. The mining industry is incredibly cyclic. So you go through these continual boom-bust phases, and I think around 2004 or '05, there was yet another bust. I think I rode four of them, boom-bust cycles, in 15 years. It's kind of crazy. So around that point, then, we figured we needed to diversify our portfolio and we started to get interested in robots for environmental monitoring. So we started to think about robots that fly and could monitor forests and creeks and coastal strips, and also underwater robots. There's a great big barrier reef, off the coast of Queensland, which is north of where Brisbane is, and we thought, "Well, that could be pretty nice. We could do – we could build special robots for tropical reef survey, and then we'd have to go to tropical reefs." <laughs> So we started a big activity in underwater robotics, as well, and both the aerial robots and the underwater robots that we built had vision systems in them. So they use vision to work out how they were moving with respect to the environment to detect things that they might collide with and avoid. So there's kind of this thread of vision going through the work for all that time. 

### Sensor Networks

Q: 

But was this the point in which you sort of branched out into sensor networks as an interest? 

Peter Corke: 

Okay. So the sensor network thing is a thing that quite orthogonal to everything else that I'd done before, and this started I think about 2000 – around 2004. A good friend of mine, Daniela Rus, and at that time she was at Dartmouth College. She later moved to MIT, and she gave me a bunch –I think six –wireless sensor network devices. I can't remember exactly what model they were. But they were quite primitive, but they were kind of cute. Those tiny little things with a radio on it, computer. You could program them and they could talk to each other and do interesting things. I got interested in what they could do for environmental monitoring, as well. So you could have robots flying over and looking from a distance, but you could have these things actually embedded into the environment. So we looked at these things and these were sort of first generation wireless sensor network nodes, and the engineer in me said, "These things aren't very well built." So I had a really good team of engineers, electronics guys, software guys. So we decided we'd build our own wireless sensor network device, and there were several generations of this thing, but we used it for quite a number of environmental monitoring applications, and so we put them in underwater environments. We put them in rainforests. We put them on sugar farms. At one point, we put them on animals. 

Peter Corke; 

So we actually put them in special collars on cows and monitored where the cows were going and what they were doing. So we'd actually build these maps of space and time and animal behavior. So we could tell when they were resting, when they were ruminating, when they were walking, what speed they were walking at, and this provided data that was – just amazed animal scientists within CSIRO that we work with. Because they had such primitive ways of acquiring data about what animals did, very labor intensive. They'd build towers with binoculars and look down and make notes on bits of paper. So we just put this thing on an animal, download it, and they just had the most gorgeous data. 

Q: 

So what kind of things did you learn about the cows? 

Peter Corke: 

I learned about how far they'd walk in a day, and from that then, the nutritionist could look at how many calories they expended in a day and therefore how much fodder they should be eating. We learned how they – animal people call it how they utilized the pasture. But it basically means where they eat from, and they don't eat a pasture uniformly. They eat it very un-uniformly. How many times they go and drink, who they hang out with, so there was this great range of information that nobody had ever seen before. They get up in the middle of the night and wander around for a bit. So there was just a wealth of data and it was just streaming out of these devices that we put onto the animals. And we took it one step further and said –and this is not our idea; this is a pre-existing idea, but we implemented it –that if the device on the animal knows where the animal is and you've got – you don't want it to – you want it to stay within a spatial region, the traditional approach is you put up fences. You can actually program the device to emit an aversive stimulus to the animal to stop it crossing a line. So the aversive stimulus is a noise followed by an electric shock. It sounds pretty terrible, but it's not that bad. The shock is no worse than electric fence. The animal quite quickly learns to associate the sound with an impending shock. So after three, four learning episodes, as soon as they hear the noise, then they just stop going in that direction. So you can keep animals in a spatial region without a physical fence. The advantage of that is fences are expensive to put up. They get washed away in floods and things like that. And in northern parts of Australia there are huge properties, hundreds of thousands of hectares. So fencing those things is real expensive. So the dream was that this would replace all of that. And we did experiments working with some really – some brilliant animal behaviorists within CSIRO, demonstrated that it worked. We could move the fences around. You could have different fences for different animals. You could separate them by sex or by age or whatever. But it didn't – it ultimately didn't go anywhere, and it's probably the project that I'm, in some ways, the most fond of and would love to get back to. It's almost – it's sort of fringy robotics; right? Sort of putting a device on an animal that makes it behave in a particular way. It's a control system. <laughs> 

Q: 

That's great. So for the underwater wireless networks, did you have to use acoustic? 

Peter Corke: 

So this was some joint work, again, with Daniela Rus, and I think by this time she was at MIT, and acoustics is a normal way you solve this problem. But acoustic modems are expensive, kind of energy hungry, and miserably low bandwidth, and because they're emitting an acoustic signal, they interfere with one another, so only one can be talking at a time. So what we want – what we decided to do or what we decided to investigate was to put a node on the sea floor, and it had a short range optical communications link, and so what would happen is the underwater vehicle, the robot, would come along. It would begin a negotiation with the node, using optical signaling, and then the device would upload all its data optically to the robot, and then move on. So the node didn't have to actually expend spend very much energy. It's not sending an acoustic pulse over huge distances. It's sending optical pulses over quite a short distance. So it's very energy efficient for the node. Not so energy efficient for the submarine because it has to swim around and visit all the guys, but it comes home and you can recharge it. So it was an interesting way of exploring some sort of asymmetry. One guy takes a big hit on his energy expenditure, but it comes home and it's actually not too problematic. Where the guys are out in the field for a long time don't spend very much energy at all. So this was a sort of interesting bunch of work where you've got sensor networks, which has got its own research community; and robotics, which has got its own research community. But actually with these two types of devices together, you can solve problems in a different way than using either one individually. So it was an interest for quite a few years, looking at how robots and sensor networks could cooperate, and also, in this work with Daniela we looked at how robots could actually deploy sensor network nodes on the sea floor, pick them up, move them, reprogram them, and we did some work with – this is with Daniela and with Gaurav Sukhatme at USC, using helicopters to deploy sensor networks, and we dropped nodes out of a robot helicopter on the ground. If the network was broken, we could drop extra nodes in to repair it. So it was an interesting research area, quite sort of different to anything that I'd done previously in my career. 

### Collaborations

Q: 

So can you tell me a little bit about your overall collaborations with Daniela and Gaurav and how you met and came to collaborate? 

Peter Corke: 

Sure. I first met Daniela, I think, at an ISER. That's the International Symposium on Experimental Robotics that Bruno Siciliano organized on a little island off the coast of Italy. That's probably not true. Actually, I think I met her first – I organized an earlier version of that meeting, which was in 1999 in Sydney, and I think Daniela came to that. But I probably got to know her better at the one in Italy. She introduced me to Gaurav, I think it was at an IROS in Switzerland that Roland Siegwart organized. And, yeah, I think, just sort of have a good rapport with both of them. And sort of research interests meshed so, I’ve had some of Gaurav’s students, and some of Daniela’s students have come to visit me in Australia. And I don’t think there’s – hasn’t been much reverse – I don’t think there’s been any reverse traffic, but yeah. So it made some of their students have come to visit me and I’ve certainly spent time at each of their labs and collaborated, written papers with them and their students. 

Q: 

Have there been any other important collaborations in your career? 

Peter: 

A couple of others. In the area of this vision based robot control, it’s a topic that’s also called Visual Servoing. Servoing is sort of a strange made up word, but anyway it stuck. The sessions here at this conference on visual servoing. So I – when I was at the GRASP lab, I met Greg Hager, he was a student at GRASP lab or just a finishing student at GRASP lab when I was there. So around ’94 or something like that, Greg pinged me out of the blue to help organize the workshop on visual servoing control. ‘Cause that was an area of interest of his, as well. And a guy that Greg knew, Seth Hutchinson , also. So Greg, Seth and I organized a couple of ICRA workshops on visual servoing. And then we – we then – actually it was Greg and Seth organized a special issue of IEEE Transactions on visual servoing. And for that they wrote a.... paper which basically was a tutorial on the field. And so they’d sort of setting up to write that and then they invited me to join that paper. That’s probably the most famous paper that I’ve ever – is definitely the most famous paper I’ve ever written. It’s got a ridiculous number of citations. So it’s Hutchinson, Hager and Corke ’96. And it’s – I’ve often cited paper in this area of vision based control, visual servoing. So that was a pretty productive relationship there. I spent a sabbatical at University of Illinois, which is where Seth Hutchinson’s based in 1999. So sort of 10 years after the GRASP Lab trip. I spent some time working with Seth and with Mark Spong there. And did a bit more visual servoing stuff and so another quite well known paper with Seth came out of that visit. I’ve got a colleague at the Australian National University, a guy called Rob Mahony, who’s another control system guy, also interested in visual servoing. So I’ve done quite a bit of work with Rob. He and I’ve got sort of a mutual friend Francois Chaumette whose from an InriaA lab at Rennes in France and so Rob and Francois and I have written paper – Francois and Seth and I have written papers. So there’s many combinations of these people active in vision based control. 

### Professor at Queensland University

Q: 

Great. So how did you wind up at Queensland University? 

Peter: 

So, towards the end of 2008, I was frustrated for whatever reason with the place I’d been at, I think it was trying to get the timing of this right, but I think I turned 50 in 2008 and I also got a letter from the management at CSIRO saying “Congratulations on 25 years of service.” And I thought, “Whoa, bad set of numbers.” So I spent half my life working here and I probably – so I think it was a bit of that, was a bit of frustration with the place, and just a phone call out of the blue one afternoon from somebody I knew at QUT saying, “Would you consider coming?” So I thought, “Yeah, sounds a bit interesting.” So I did an interview and was offered a position as professor, thought that was pretty cool. I think probably figured one day I was going to be – become an academic or a professor. But it took a while to actually happen. So I think that interview was in around 2008. I had a lot of holiday built up and so I thought, I should take the holidays. So 2009, I spent a lot of time on holiday. And that was when I started – I started writing a book. So yeah, that happened that year. So I’d spent 3 months in Paris, living a writerly existence, just me and my wife, in a little tiny apartment and yeah, started writing a book. And after that, spent a few months in Oxford and wrote some more books. Then most of the next year finishing the book, and... 

Q: 

This is the visual control book? 

Peter: 

Yeah, so it was – I never really planned to write a book but I’d sort of thought about it on and off, and I got going I just – it just kind of all came pouring out. So it’s a behemoth of a book, there’s about 600 pages, but it all had to be said. And yeah, I enjoyed the experience of writing it. So yeah, it was kind of a long drawn out transition between – between CSIRO and the university but I started there in January 2010. 

Q: 

And as you were writing that book, so what did you see as the necessity of writing such a book that nobody had sort of brought together all the work and visual control before? Or was it that there wasn’t a sort of an overarching theory before? 

Peter: 

It’s not a theory thing. I’m not a very theoretical person. I’m not a very, very mathematical person. I probably tend to think a lot in diagrams and simple concepts and there are a few things I thought were missing from the set of text books that were out there. One is they all had a fairly formal mathematical approach to robotics. Another aspect is that in terms of what you can understand treating robots formally, mathematically, it’s hard to go much beyond a very simple robot, a robot with two-joints, or robot that moves like this. A robot, a real robot with six degrees of freedom or more, you just can’t write the math’s for it. It’s just too horrible. And so, one concern of mine was that these books kind of lacked the inside into real, real robots. ‘Cause they use mathematics, they kind of go to robots of the sort of complexity of the robots that we actually use, that was one consideration. I’ve had some open source software that I’ve written over a long period of time, I think with a robotics toolbox for MATLAB. Just came out of my Ph. D. work, and I kind of tinker with it in bursts ever since. But it allows you to actually solve problems with practical robots with six joints, or eight joints, or whatever. And so I wanted to fold that into the book somehow. So the book is, I like to think of it as a bit of a narrative, but it uses the software tools to help you solve the problems. So, it doesn’t get too much into the theory, but it allows the reader to get their hands dirty and solve quite complicated problems, quite quickly. And motivation is that, okay if they find that interesting and they want to know how it works, then hey, there’s a lot of really other good books that they can go on and read. So I didn’t want to replicate what the other books did. I wanted to try and get people engaged and solving realistic problems with minimal pain, getting excited and then wanting to go and learn robotics. So there’s a bit of a sort of inverted approach to learning. So that’s probably the main thing about the book. The book doesn’t have that many equations in it, but it’s got lots of bits of code. So you can open any particular page of the book and there’s some code that says, “This is how you make a robot do this.” So you can actually type it into MATLAB and replicate the result. And you can plot the data differently, you can change the parameters, change the robot mold, it’s, yeah. 

Q: 

How have you found it different to be working in an academic university setting as opposed to a company? 

Peter: 

The – there’s a couple obvious differences. One is ways around freedom of what you do. So it’s CSIRO, increasingly the research agenda was set by other people, not by me. So at the university I can do a research, really on anything that I want to do, I guess as long as I’m training students and, or, generating some publications along the way. So the freedom is a big one. The second one is probably resourcing and funding. At CSIRO, the funding was much more – much more lush than it is at the university. The university, its hard work to get funding, you got to write grant proposals and then wait for them to come off and all of that. So university more freedom less resource, the other place more resource, less freedom. So yeah, that I think the fundamental trade. 

Q: 

But you adapted well. 

Peter: 

Yeah, I think so. Been successful in some early, early grants, and it’s got some good colleagues at the university. So when I went there, I’d sort of dragged a few other people in as well. So we started with a good nucleus. And the university has been generous in funding us with extra, extra positions. So we’ve got quite a good vibrant lab. And that’s a joy to have sort of built this group up. 

### IEEE Robotics and Automation Society

Q: 

So you can tell me a bit about your history with the IEEE Robotics and Automation Society. How you got involved with it? 

Peter: 

Sure. 

Q: 

Can you tell me a little bit about your history with the IEEE Robotics and Automation Society? How you got involved in it? 

Peter: 

I think I’ve been a member of the IEEE for the longest time. Probably since I was – did my Ph.D., and I’d come along to ICRAs and IROSs and those sorts of things, subscribed to the Transactions and the magazine. Probably never paid too much attention to how the whole organization worked. Didn’t – probably early on didn’t realize all the people slaving away to make those things happen. I can’t quite remember how I got involved in the society. A colleague of mine in Australia, Alex Zelinsky and Oussama Khatib leant on me a bit to join the ADCOM. I didn’t even know what the ADCOM was at that point so, I think I – I can’t remember what year I joined the ADCOM, I could probably work it out. ‘Cause I get kicked off this year which is 2013, so I’ve been on it for four years. So it must have been 2009, or thereabouts, that I’d joined the ADCOM and that was probably really my first introduction to what was going on behind the scenes. So the ADCOM’S like the parliament of the society. So we’re elected by the members, there’s 18 of us at any one point. And it’s our job to keep the executive under control. And yeah, so I was then on various kind of subcommittees. So yeah, got some experience around the society about how it worked. And.... I’m trying to remember the year that I got involved in the magazine. It was the year before I went to QUT, so it’s also been 2009, I was sort of – they’d asked me if I’d be interested in their editor-in-chief of the magazine. Reason being that Stefano Stramigioli who was the editor-in-chief of the magazine, he’d been tapped on the shoulder to become Vice President of Member Activities at the end of 2009. So he had to step – he was doing too much. So he had to drop something. So he decided he would step down, and there was a search for an editor, and they asked me if I was interested. I think I initially said, “No.” And then I sort of thought about it and thought, “Yeah, that could be good.” I had been on their editorial board for the magazine back in the early 2000’s. I think, I think I served two terms as a member of the editorial board, or as an associate editor, is the correct notation for the magazine. So I had some experience with the magazine. Had soft spot for the magazine, so yeah, it was a delight to work as editor-in-chief. 

Q: 

And what were your sort of most accomplished issues as editor-in-chief, the ones that you’re proudest of? 

Peter: 

I think there’s a few things that I’m proud of the magazine. One was moving it to electronic delivery or something. And I think was important to a lot of members. Around that time, everyone started tablet – tablet computers suddenly appeared, right? And tablet is the marvelous means to read a magazine. So it seemed really timely that we should have the magazine coming out electronically. So you just download the file and browse it on your tablet. I think the magazine had struggled for a long time to work out quite what it was. It’s not exactly a trade magazine. It’s not exactly a Transactions, and it’s a – it’s an odd beast and that was initially, I think the reason why I said no to becoming editor-in-chief, and I sort of thought about it a bit. And – it really... it really should be a magazine and not a Transactions lite or anything like that. So, it’s one push probably all through my editorship was I used this word “magaziney” I wanted to make it more magaziney, and the production people didn’t like the word, magaziney but I stuck with that. And so my criteria for an article really was, is it – if I was a reader would I find this an interesting article to read? And a lot of the – when you send – an article comes in and most people in its community write articles like they’re transaction articles. They’re quite formal, they got a lot of math’s in them. For a magazine you don’t want that. I want an article that tells a story that’s got quite a lot of good graphics or pictures or whatever. And I think people in this community feel uncomfortable writing like that. My theory is that they use the formulas and the maths as some kind of ward of the blows of the reviewers. So the first thing was to try and convince people that it’s okay to write an article like that. That’s readable by somebody who’s not in your narrow technical area. So someone who’s got some technical background, but not in your specific area. And the other thing then is the reviewers. And the reviewers are also trained to attack any paper that’s presented to them. And the most common criticism for reviewers is always, “No contribution.” And it’s something you really can’t refute if a – if for a Transactions if the reviewer says, “There’s no contribution. No novelty.” Then doesn’t get up, it doesn’t go into the Transactions. But for a magazine, I don’t think it matters if someone else has done it before that’s okay. But if someone can tell the story really well, nice words, they explain it adequately, it’s got some good images, I don’t care, is it a good story for the reader? So I tried to turn that around if reviewers came back and said, “No contribution.” Then I’d say, “Well actually, that’s not a valid criticism for the magazine.” And it took a while I think for reviewers to understand what the magazine wanted. Took a while for authors to understand what the magazine wanted. I’m not sure we’re completely there yet, but I think kind of pushed the thing more towards being a magazine and less being a Transactions. The other thing I thought was important for the magazine was columns. So you – some regular columns in the magazine to just to lighten the mix a little bit. So there was a ROS column which Steve Cousins wrote. Who just said what’s happening with the ROS project. ROS was starting, started a bit before I became the editor-in-chief. But it seemed, it’s a massive contribution to our community and they should have a soap box where they can just, tell us what’s going on. And there’s a bunch of other, sort of regular columns that I initiated. I probably initiated more columns than was sensible. ‘Cause often times, not every column ran every issue. ‘Cause it was just hard to get the content and I tried to do a little interview piece which appeared at the back of the magazine and it did for probably the first half dozen issues, and then things just started to get away from me. And that interview fell off, and life got more and more complicated, and so eventually I stepped down as being – before the end of my term, because there was just too much going on. But people like the little interview piece and I liked doing it, but yeah, just not sustainable. 

Q: 

So, well apart from the cows and the ’96 paper, are there any – anything we overlooked that you look at as your sort of proud achievements in robotics or papers that you’ve done? 

Peter: 

No, I don’t – I don’t think so. I think that the ’96 paper’s important. There’s been some great collaborations with a number of people all around the world. Book, I’m pretty delighted with, people are reading it and using it and for teaching and things like that. The open source tool boxes are still really widely used. There’s an active user community and that’s a source of delight. I’m working at the moment on doing an open, online robotics course. Seemed like a good idea when I mentioned it, now I’m up to here in the project and it’s totally massive. I’ve – another thing that I underestimated. And we hope we’ll run a beater at the beginning of next year and hope to offer it globally for northern spring semester of 2014. That’s the plan. So I’ve been doing lots of, lots of videoing, and narrating, and working with graphic designers, and learning designers, and software support people, and it’s a brilliant project. And I wish I was doing it full time, but I’m doing it with about ten percent of my time at the moment and that’s – it’s hard. But this is probably the most exciting thing I’m doing at the moment. 

### Ph.D. Students

Q: 

So you’ve only been at QUT for a few years, have you trained some Ph.D.’s in that time? 

Peter: 

Not quite. I have at the – so I started with three Ph. D. students. Two of them are just about to start writing up. So in Australian system Ph.D.’s typically take between three, three to four years. So yeah, two of them are just starting to write thesis now and they should be graduated the beginning of next year, and I’ve got some more recent Ph. D. students starting. So somewhat – I’ve got something of pipeline happening. So that’s pretty exciting. I’ve been what we call an associate supervisor of Ph. D. student’s before. So – because I wasn’t an academic, I could never be their principle advisor. So been associated with four or five in the past, it’s not a great number, but now I’ve got a couple of my own almost done. 

Q: 

And are they working in field robotics or what areas are they in? 

Peter: 

The two are both in field robotics. One in QSAR is Korean student of mine and he’s working on flying robots. And the quadcopters which are very popular at the moment, and you see some fantastic results with quadcopters. You see them playing, juggling balls and moving synchronized to music and whatever. But all of those quadcopters are operating in environments they call Vicon motion capture environment. So there’s this big room with all these fancy and expensive cameras around it looking at the robot and telling it where it is very accurately and very often. A thousand times a second it gets its position to millimeter accuracy. The real world’s not like that. So, my project with Inkyu is to say, “Okay can we put equivalent sort of sensor capacity onto the vehicle itself?” So kind of turn it inside out. Put a vicon light capability on the robot. And so we’re using high speed camera on the robot itself. Not as high speed as the vicon but still fairly high speed and using it to maneuver next to fixed infrastructure. And so, vertical pole inspections to specific problem that we’ve chosen. So, my goal to him as, I want to be able to fly this quadcopter, really close to a pole, safely, even though I’ve got no skill. So the skill is in the quadcopter. It can sense where it is with respect to the pole. And through the joystick, all I simply say is go up and down, or go left or right. The actual hard work of flying it and keeping it where I want it to be is done by the machine. So that’s one project. The other project by a student of mine called Steve Martin is concerned with... with ground – outdoor ground robots sensing the characteristics of the ground that it’s driving over. So by looking at the power it’s exerting to drive over terrain, it can say something about its traverse-ability. And so he’s been doing some mapping and then some path planning. So by driving around it can learn what’s an easy place to drive and what’s a hard place to drive. And if it’s got some goals that it’s got to visit, then it – as its learning through experiencing the environment, it can iteratively improve the path that it takes to visit these locations using minimum amount of energy. So that’s a nice piece of work. 

### Robotics Experiences

Q: 

Great. And one thing we often ask, is any spectacular robot failures? Or funny stories that you’d like to share? 

Peter: 

I mean, probably quite a lot of robot failures. The one that’s probably most mortifying as a controls guy is when we’re doing some early work on these big drag line excavators. There’s these massive three and a half thousand ton machine. And we – it rotates on its base. And so I was writing the motion control software for this and wanting it to rotate. And I got a sign wrong. So instead of negative feedback on this thing, it was positive feedback. So you run the code, the whole thing just started moving really quickly and getting faster and faster, not slower. So yeah, that was – that was spectacular. I mean, did what theoretically it should do, but it was on a very massive machine that I’m sitting in, right, with – I mean, half a dozen other people are sitting in it as well. It was embarrassing. 

Q: 

Did you have a kill switch, I hope? 

Peter: 

Oh we did. It just took a minute to where – “What’s going on.” Whack. 

### Advice to Young People

Q: 

Okay, good. And what’s your recommendation to young people who might be interested in a career in robotics? 

Peter: 

You should do it. Robotics is going to be, it’s going to be a really big thing in the future. I mean, you just think about ten years’ time are there going to be more robots in the world or less? There’s going to be more because there’s a whole bunch of, I think, societal pressures which are going to cause more robots to be adopted in society as demographic shift, as a population we get all the – there’s a whole bunch of labor still needs to be done but I think there’s going to be less people to do it. There’s – I mean, agriculture which is a current interest of mine, there’s going to be more mouths to feed on the planet. There’s less land because of urban encroachment, the climates changing, all sorts of things. I don’t think we can produce food, as much food as we need, unless we adopt technology like robotics. It’s going to be – it’s going to be important in health care, which is something that in most societies just can’t afford the healthcare that their citizens expect. And I think robots going to play an important role there. So labor intensive. And there are some jobs that are simple enough robots can do them now. And as robots get more capable, then they can do more and more sophisticated tasks. So there’s huge, huge opportunities in robotics. So yeah, get into it. 

### Future Challenges

Q: 

Now what do you see as the biggest, kind of, theoretical or technical problems facing robotics over the next five to ten years, or beyond? 

Peter: 

I think it’s probably just picking... picking the right problems to solve. I think a lot of the technologies, techniques we want are already there, I think we have sufficiently good techniques. I think we often don’t have is the business case. But I think in general, it’s not the techniques, it’s not the computers, they’re not what’s holding us back, I think we’re probably not focusing on the right problems. So it’s the com – the problems really around the commercialization of the technology. 

Q: 

Is there anything that we missed? Anything you would like to add or talk about? 

Peter: 

I don’t think so. It’s been a good chat. 

Q: 

Yeah, it went really well. We got through a lot, very quickly. 

Peter: 

Yeah. 

Q: 

That’s great. Okay. Thank you. 

Peter: 

No worries. 

Retrieved from " https://ethw.org/w/index.php?title=Oral-History:Peter_Corke&oldid=182590 "
