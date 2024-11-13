
https://www.youtube.com/live/c0gcsprsFig
https://applied-llms.org/

---

This conversation appears to be a discussion among friends or colleagues about artificial intelligence (AI) and its applications, specifically in relation to foundation models. The participants seem to have a relaxed and playful tone, often joking and teasing each other.

Here are some key points from the conversation:

1. **Foundation Models**: One of the participants mentions training a foundation model from scratch using $50 million in DC money ( likely referring to deep learning computers). This is presented as a key step towards achieving success.
2. **Iterating to Success**: The group discusses the importance of iterating on ideas, similar to Charles' "zero to one" approach. They compare this process to traditional experimentation with new products.
3. **Offline Experimentation**: The conversation turns to offline experimentation, where evals (evaluation metrics) are used to quickly cycle through different versions of a product.
4. **Zero-to-One Improvements**: Participants discuss focusing on small, incremental improvements that add value to the user experience.
5. **Collaborative Effort**: The group expresses appreciation for their collaboration and the resulting media report, which has had a significant impact on the community.

Overall, this conversation seems to be a lighthearted discussion among friends or colleagues who are passionate about AI and innovation.

---

All right. Hi, everyone. Hugo Bown Anderson here. I'm so excited. I could barely sleep last night. I'm here today with, currently with Eugene Yan, Shreya Shankar, and Hamel Hussein, who I'll introduce, of course. Their co-authors will join us very soon. But what I'd love to do is we're going to start in a minute or two. If you could introduce yourself in the chat, let us know where you're calling in from and what your interest in this type of stuff is as well. And also what you'd like to get out of the session. Do you, are you building LLM systems currently or working AI, data science, or all of these things? So let us know in the chat and we'll get started.

My name is Hugo Bown Anderson, and I've worked in data science and machine learning and education for a while now. And this is a live stream for a podcast that I do called Vanishing Gradients. And I'm just going to put a link in the chat here. And this is, whoa, whoa. Yeah. I'll put a link to the podcast. And then we have, we have a lot more live streams coming up, and I put them on Luma. So I'm going to put the Luma there as well.

And excitingly, I've got, we've got a bunch coming up, but two of my next guests coming up soon are going to be Shreya Shankar solo, who I haven't spoken with in public solo for some time. So we're going to be talking about evaluations and how to evaluate the evaluators and what that means and the cool products and research she's doing. Another guest will be Hamel Hussein, who we have here. Again? Wow. Dude, yeah.

And so Hamel is, everyone here has been on a real journey as of late, but Hamel and our dear friend and colleague Dan Becker recently taught a course which blew up into a conference. Everyone here spoke at it. And Dan and Hamel, correct me if I'm wrong, Hamel, but you thought maybe you were going to teach a couple of hundred people. Turns out 2,000 people enrolled became a multi-sided marketplace with products and vendors and open source frameworks and speakers and learners. So we're going to have a podcast episode on what they learned teaching LLMs to thousands of people around the world.

So I've just put the Luma Calendar link in the chat. Got lots of people tuning in from around the world doing all types of different stuff with LLMs, which is super cool. I honestly think, without further ado, we should get started. I do want to say, if you enjoy this type of thing, please do share with friends and hit the like and subscribe because we do a lot of stuff like this. That'd be super cool. But without further ado, let's jump in.

So to set the scene, over the past year Eugene, Shreya, Hamel, and their co-authors have been building real-world applications on top of LLMs and have identified crucial and often neglected lessons that are essential for building and developing AI products. And they've written a very meaty report on the lessons that they've learned, which I'm going to share in the chat now. But I would love, if we could start off, maybe just go around and introduce yourself, maybe starting with Eugene and let us know why you're even interested in LLMs.

All right. Hi, Ron. I'm Eugene. I sell books at a bookstore, literally. I work for Amazon Books. But that's it. Opinions here are my own. So my work is really around recommendation systems and search. But recently, I think large language models can help readers, customers understand their recommendations and search a little bit more and just add a little bit more life to it. So that's how I'm thinking of using large language models to try to help customers understand their recommendations and search.

Amazing. And to be clear, you build Rexis, among other things, that millions of people use worldwide, right?

Yeah. I used to do a lot of Rexis. I think my first three or four years was really focused on Rexis. By the last 18 months, I've been trying to catch up with what's happening in language modeling and I'm still struggling to catch up so that I can figure out how to serve it reliably.

Absolutely. How about you, Shreya? What's your background? What led you to this wonderful world of LLMs and thinking about evals so much in particular?

Yeah. So I am a researcher and also ML engineer. I'm doing my PhD in data management and UX or HCI for machine learning. Why am I interested in LLMs? I think most people, myself included, want intelligent software and many people want to build intelligent software, and LLMs make it super easy to do this, not just prototype it, but really to get it into the hands of other people and create a very simple flywheel to learn from. What are the errors and how can we really quickly iterate on it? Yeah, very simple.

Great. In particular, though, you've always had a deep pathological interest in databases. No, I'm joking about the pathology of it all, but hopefully something we'll get to is, once again, the importance of the data. So maybe you could just speak to your interest in databases more generally.

Yeah. Well, I think all ML problems are data management problems to some extent. And you can look at it in a lot of ways. What are the right samples of data that we use to solve problems? How do we quickly incorporate data? How do we quickly iterate on these systems to improve them? And a lot of it just comes down to how do you help people manage their data better so they can build these intelligent products? Databases are one way of thinking about doing it, but databases do a lot of things, so can't really compete with this little bit of software.

Absolutely. And just before we move on to Hamel, which I'm really excited to get to, can you please introduce your friend?

Oh, this is my dog, Papaya. He's very happy that I came home from the lab.

What a cutie. What's his interest in LLMs? Is it just through?

He doesn't even know what it is. It's probably for the best. The good old days when we're all naive. Ignorance is bliss.

So Hamel, what are you up to? What's your interest in LLMs? I mean, you have a decades-long history in ML and these types of things.

Yeah. So yeah, I've been doing ML for 25 years. I've worked a lot on infrastructure like tools for data scientists and machine learning infrastructure and developer tools. I started working with large language models early on at GitHub. I led some research that led up to GitHub Copilot around large language models and code understanding. Yeah, I've just been doing it for a while. At this point, it doesn't make sense to do something else. So it's not so much like why is it interesting? It's like, well, it kind of feels dumb not to keep doing it because they're so powerful of the technology.

So I haven't really stopped to think about, I don't know. I never really thought about like, why is it interesting? It's like, well, yeah, this seems like, obviously, like a powerful technology and yeah, very helpful in many respects.

So yeah, I love that you're like, it's just what I'm doing now. But then you speak to the power. And I think the power of these systems that we're still, you know, working hard to understand. We talked about this recently, as part of your course, right? But Simon Willison has a video where he actually referred to LLMs as fractally interesting, that you can look at them at a lot of different scales and all types of interesting things emerge. And I do think there's so much to discover in there.

Yeah, one thing I'm interested in the most is probably the most is like how to really speed up the software development life cycle with LLMs, like how you can code faster, launch applications faster with a smaller team. I haven't worked specifically on that area, but it is like probably the thing that's the most, like I haven't worked on that in a while. But I think it's pretty interesting.

Yeah, absolutely. And I do think, you know, some of the things you all think about and what you work on, Shreya, in terms of, you know, human-computer interaction stuff, you know, speaks to this and making sure that developer experiences are as frictionless and smooth as possible.

But hey, we've got a lot of people saying they've read the report recently, or they've read part of it in there. Someone says lovely dog. So Papaya, I mean, clearly everyone, who could not think Papaya is a lovely dog. But this is a beast of a report. And I love how, you know, you go through tactical, operational and strategic things like position towards different parts of an org who may, you know, really need to wrestle with all of these issues.

But I'm interested with you six authors. I know you've all known each other and been friends for some time. But what, how did this even get started? What's the origin story of this report?

Oh, okay. I guess. Yeah, I guess we were just chatting in our chat. We have a group chat, small group chat. We were just chatting about how you were thinking of, I don't know, Brian was talking about something, and he was talking about creating slides, you know, let's maybe discuss during our office hours. And then he was saying that he was thinking about writing about a year of LLMS. And I'm like, dude, I'm like drafting it right now. And I took a screenshot of my obsidian note. And it's like, it's like, ha ha. Okay, then we just left it at that.

Then Charles gave us the next night, just like, guys, it'd be cool if we just collab. And then of course, Hamo was like, Hamo and Jason just, yeah, let's do it. And of course, the first thing I think about is Shreya, right? Shreya, I really want to work with you again. I mean, I've worked with Shreya on several of my own writing. Shreya has been an amazing editor. And I've also chatted with her about her own work. So it's really exciting. And that's how it came about. And then, okay, everyone write your ideas, we just figure out how to mishmash and merge them. And that's how it happened.

So I think, I think you spoke about technical operational strategic, right? That was how Brian thought about organizing, right? And I think, I'm so glad that he actually did that. Because there's just, there's a lot in there. I think there's 40 something different lessons. And by organizing it at different levels, I think it just makes it easier to consume. So I think that's how it came about. And of course, the moment I asked Shreya, she was like, yeah, man, come in. She was just so game. I was just so happy that happened.

Awesome. So I'm interested in, we’ve already mentioned evals. So I've got a question for you, Shreya. The report really highlights a lot of work and stuff you're doing on evaluating LLM output quality. Can you share more about your approach to this challenge and how it differs from what we've seen in traditional data quality?

Yeah, I mean, this is very kind. First of all, other people, other authors wrote about my work. And there's no greater pleasure than having other people write about things that I'm researching. I think there's two main things that I was thinking about. One was when you consider real world data quality, right? So not Paul Graham's essays, which every single LLM has been trained on, or collections of data that just are so, have permeated the internet a lot. How do a bunch of evals perform, right? For example, canonical needle on a haystack queries. I just had this question, try to conduct a bunch of experiments and learn some really interesting things. For example, when there are typos in the input data, or the casing is a little bit different. When you ask Mistral to retrieve a name from a document, and the name is lowercase, Mistral fails to retrieve it. Small idiosyncrasies like this are really hard to uncover in traditional evals. And I don't know how to study this further.

I think the report that we wrote makes one step towards in pointing something out. But there's still quite a long ways to go. The other thing around evals that we talked about in this report was just generally, how do you think about validating the valendars? How do you construct a flow to give you the right assertions and evals to deploy? This is really hard because one people don't know what concepts they should check for in their outputs, right? This itself is a function of the LLM outputs. You have to look at hundreds of outputs to even know what are the weird failure modes in LLMs and what, at the end of the day, do you care about as a developer folding? So it's kind of doing this process and flow.

It's dog is stretching. We wrote about this in the paper, in our eval gen paper. And that kind of flow made its way towards this applied LLMs report, which I thought was very exciting. And I'm happy that it resonates with Hamel, Eugene, and the others.

Well, yeah, I actually wrote about it. I actually put it in. I'm like one of, maybe I'm the biggest cheerleader or one of the biggest cheerleaders in the world. I appreciate that. It's because like, okay, like people, every time I talk, I'm helping people in the wild with large language models, they really struggle with evals. Like, how do you get started? How do you think about it? What do you mean, write a test? What does the test look like? Should I just write like unit test? Is it like high test? Like, they're like mentally like a writer's block and just like don't know where to begin. And they get really, they like people shut down. They're like, this is so hard. I don't even know. I need like, I need some expert to help me. I'm stuck. There's no way I can do this. This is like beyond my capabilities, whatever. It can be really easy to get overwhelmed.

But actually like, okay, so like my daughter, who is five years old, she's learning programming. And like, it's really interesting. Like, if you, you know, there's these amazing applications, like, or like languages like scratch that are like really fun and approachable, and like teach you that programming is, is, doesn't have to be hard. Like, you know, it can be fun. And so one of the things that I noticed with Shreya's tools, like that were part of a research, it was kind of like scratch for evaluations, like visually showed you how to think about it. You could like build these building blocks and then like, sort of, it would help you generate evals and different kinds of evals and like validate them. And what I saw in that, I'm like, wow, okay, this is kind of like scratch for evals. And I would show it to my clients. They would immediately say, say, like, oh, I get it. I like finally understand what to do. And yeah, super powerful, like super powerful teaching tool, honestly. And yeah, I think I told Shreya, she was like, maybe a little bit surprised at first that that's the angle of the work.

Like, I'm like, yeah, it's teaching. I use it for teaching. No, I'm thinking about it a lot. Like, we collectively are teaching people the processes. We're not teaching people tools. We're not teaching people how to use LLMs. We're teaching people how to do the strategy around, okay, I'm committed to building this AI product. How do I go about doing it and making sure it works in one year from now? It's like, still there and people using it. Like, that's, there's so much work, I think, to do in that process oriented mindset.

So when Shreya said Hamel might be one of the bigger, one of the biggest celebrators of my work, I was going to joke that Hamel just doesn't stop talking about it. But then he launched into it immediately, which I love. I am Eugene, you actually prepared a question for Shreya, which is related to this conversation. So maybe you could ask that now.

Yeah, I guess the question I have for you, Shreya is why are you so bullish on LLM evals? LLM, LLM based evals, LLM as a judge or LLM as a evaluator?

It's like we've never talked about this before, ever. Oh man, a lot of reasons. So I think there are a lot of people who want to build LLM powered software that don't have the resources to do, you know, traditional monitoring and evaluation that traditional ML products would have. Like, it's one person team, two people team, very small startup, very early stage product, and they just, they want to ship quickly.

I think there's also people who just cannot collect the data that they need to be able to write their own evaluate, fine tune their own evaluation models. And to have all of these barriers seems very challenging and at odds with the simplicity of deploying LLMs in the first place. Like if LLMs are so simple to deploy, we need to have somewhat of a simple evaluation method. Otherwise, like, what's the point?

And then the other argument here is, you know, these LLMs are getting much cheaper and much faster for the same, I hate to use the words intelligence, but I don't have a good substitute. I don't want to go down this like AGI route. But GBT40 is great. This new Claude Sonnet model came out this morning. It's just getting faster and cheaper. And you don't have to run on all of your data. But if you sample your data every day, run GPT4 on it, GPT40, it's affordable, could be good.

Awesome. So we've really, really jumped in in a nice way, but getting in the weeds with evals. But I'm interested, Hamel, maybe you could tell us why it's so important to talk about evals as soon as possible.

Yeah, I mean, so I actually sometimes I think that maybe I should just not even say the word evals, because it's like when I see you say the word evals, then people start looking at you like you're some kind of rocket scientist or something like, Oh, like, he's using this word, like, what does it mean? And really, it's not really about evals. It's like, Hey, let's take in a like a systematic approach to making your AI better.

Like, just stop, stop fucking around and start having like a process, like you can only like just eyeball it. You know, eyeballing it can only take you so far, you know. And so it's like, Hey, it's not really eval. It's like, it's, let's measure, have some way to know whether we're making progress or not. And that that measurement of making progress, like let's make it to where it's as frictionless as possible, so that you can like know every time you make a change whether you're not making progress or not. Otherwise, like, there is no other way to make progress. And like, it's not really about evals, it is just how you work on AI.

Like, it is not a component of AI, it's not optional. It's not like, Oh, like, you should do evals, or maybe you can do it, or it's good if you do it. If you're not doing it, you're not doing, like, you're not doing any AI stuff, like you kind of maybe filling with it, and just saying, huh, I'm in the prompt and I'm using you can use AI, like whatever, if you're like building a product around it. If you're not measuring anything, then if you're, yeah, you don't have a way to make it better. If you don't wait, make it better, you're not like, how are you going to build? And so it's really just how you build. And then like, you can drill into that and say, what are the steps?

Yeah, I think it's just machine learning 101. I mean, the first thing you learn in machine learning, training set, validation set. This is the same thing. It's just validation set. Yeah, and it does, I mean, in some ways, it's a proxy for a loss function, because in the movement from classical machine learning to generative AI, it is an obvious what the loss functions are anymore. What we need to fit to. I am, as we mentioned, the report covers a lot of ground across the tactical, operational, strategic aspects of building with LLMs. I'd like to hear from each of you as to which area do you think is currently most underappreciated or overlooked in the industry from tactical operational and strategic?

I don't want to go first because my answer would change every week. Are you going to go first?

I mean, I'm going to go first, but I'm probably going to say what Hemo is going to say. I think what is overlooked is how to bring everyone along. How do you train your existing software engineers, equip them with the skills to be able to do this, right? I mean, so I think about this a lot. I work with a lot of excellent software engineers. How can I teach them to do very basic evals, create some kind of synthetic data, either use something data from Kaggle, et cetera, et cetera? How can I teach them to understand that generation is autoregressive, a longer output will lead to longer latency? It's just some of the basic things of how it works.

How can I teach them that context is just conditioning so they can be more effective in using that? I think that currently right now, I just don't see a lot of that. I don't know why. And I think about that both on my job and outside of my job. And that's what I think we haven't done a lot of. So yeah.

Shriya.

I'll tell you the one thought that I had last week. So we conclude saying something like, oh, there's so many demos and we've got to put things. I don't remember exactly what we say, but enough with the demos, let's start putting things into production. And I heard a talk at a conference that was also saying the same thing. And then I really thought there's a new demo plus plus or prototype plus plus going out there where you will see things in production and you don't somebody hacked it together over three days. And then it's a catalog product and a large cloud retailer. I don't even know what to say. And now I'm thinking how do we move from prototype plus plus to a real product?

And the bar for production has lowered a lot with generative AI. Anyway, this is such a rant. It's a tangent. It's not answering your question.

Tell us more about how the bar for production has changed.

Well, I think you can hack together something in three days that passes a sniff test for VPs. And it could go to production depending on the culture at the company. And this can also be large, small, small products. You just said both of them, actually.

Yeah, it was really confusing, actually.

Yeah, so I think it's like these products have not really been launched with evals or some sort of rigorous way to quantify improvements. And I think we're pretty far from that. I hope that the report helps people get towards that. But is this related to the issue that with generative AI, like shiny demos are a lot easier to build, but then we have this tail of all the things that arise then from hallucinations to difficulty getting in prod to not having robust evals, this type of stuff.

So you get a flash and then kind of a relaxation of some sort.

Maybe, but I think still people are putting their first things in production without having any form of evals. And I think, well, go ahead, yeah.

Oh, to me, that's not a commitment to the process, right? That's like a commitment to showcasing your demo.

Yeah, I like that. We've touched on like learning the process, which I think is key. I think that like it's worth it to linger on that for a second. So a lot of people in the space are really obsessed with tools. Like you say, hey, we should do evals. We should do, you know, we should improve your rag. The first question you get asked more often than not is, Oh, like what vector database should I use? What embedding should I use? Or what vendor do you recommend for evals? And we get like really hyper obsessed with tools and like we're not learning the process.

And that is where it's going very wrong. I think that's part of a some like that's it. That is part of a narrative, which we can drill into. But I think that's that's where a lot of people are shooting themselves on the foot is like not learning the process and focusing on tools.

So, Hamel, you've been working in and out of consulting for decades now in classic data science, ML, now all of this generative AI, LLM stuff as someone who's advised a range, a wide range of clients on AI strategies. What are some of the most common misconceptions or knowledge gaps you encounter when orgs are first exploring the use of these technologies?

Yeah, so there's one that is probably, I would say, the big elephant in the room. And really what it is is it's a skills issue and that's related to a certain narrative. And this narrative is, so you may be familiar with the role of AI engineer and the way that the role of AI engineer is coined.

I should probably share a screen or something. I don't know if I should do that. Yeah, do it, man. You're giving away the keynote. Like Hamel is bringing out his big slide, he's ready, man.

No, no, I'm not going to take a slide. Let me just hold on.

So, I guess for the audience, I think this is a sneak preview of the keynote that we'll be giving at a conference next week.

Yeah, I'm going to share my slides. What's the conference?

Oh, there's the AI engineer conference. Yeah, there we go. There's the AI engineered world's fair.

I didn't even know you believed in the AI engineer, Hamel.

There you go. Trying to, yeah. So, okay. There's this very popular sort of characterization of the skills that you need and that you should focus on in this new era of generative AI.
And it's really taken off. It's really like been, you know, it's kind of been adopted by many people across the industry. And it's this articulation of skills where, you know, you have the spectrum of different roles and different skills.

And you have this API level boundary. And on the kind of right-hand side of the API level boundary, you have something called an AI engineer. And the AI engineer is like differentiated in this new era because unlike, you know, unlike years before, to deploy an ML product, you don't need to know about these things that are listed here, training, evals, inference, data. And that you only should, you should like be mostly concerned with tooling and infrastructure, chains, agents, so on and so forth.

Like that's the thing that you should pay attention to. And so, you know, like this seemed very reasonable to a lot of people. There's some like, this is very, like, it was very persuasive in some degrees and in some circles, very persuasive, and it really took off. And lots of people hired their talent according to this narrative.

Now, I think like one thing that sort of went a little bit sideways with this narrative is that, you know, evals is not really, it doesn't really have to like have a model that you train to need evals. Like even if it's someone else's model, evals is just like, how do you measure stuff?

And evals can like the notion of evals in unit tests are actually pretty close. The notion of having evals and writing software are like very close in nature. And then like data actually is another thing, like, so data literacy.

So data is not about necessarily training models, per se. Like that's not the only use of data. These actually, it's actually useful to look at lots of data to see to debug a system. And it takes like some data literacy to, to be able to navigate data. Data is kind of messy. As you know, you go like, and everybody else like data is like really messy and like having good tools to like farce your data, navigate through it, filter it, do so on so forth.

It's actually like surprising, like it takes some skill over time. And so by, you know, sort of ignoring evals and data, and like you don't need training and inference, for sure, like those things, I would say, okay, I would agree with that. Training don't need it. If you're using API inference, you don't need it using API.

The thing that is really, this really gotten people stuck is like this evals thing and this data thing. And by kind of like making it not your concern, this AI engineer role sort of gets stuck after the MVP, and they get stuck immediately, like immediately stagnate.

And that, that really hurts. And then also the title really hurts. So the AI engineer title, just like, if you name someone AI engineer, it's the same thing as naming them AI King. Like the expectations are really high. If something is going on with the AI, like, you know, your company is building AI stuff, and you're like hit stagnation, your CEO is going to look at the AI engineers, like you're the AI engineer.

I thought your title is AI engineer. Everyone else is going to look at you and say, hey, I thought you're the AI engineer. AI engineer is going to be like, I don't know, like what to do now. I've mastered the chains, the agents, the tooling. I have all the tools. I'm like expert. I like all the tools. But like, what do I do?

And that is kind of this is where this like gap is where most of the, this is like, not most, I'll say 100% of all the consulting business come from. And I'm talking about between Jason and I, it's like, you know, Jason's not here, but it's like millions of dollars in consulting, just because of this one thing is the talent gap.

And I'll say this is like very impactful because, you know, like if you're building AI or really anything, not, not even AI, the talent that you have is the biggest impact, is it the biggest like the lever that you can pull, like what talent you hire, what skills, how you hire. And this is the thing people are getting wrong. So I'll just stop for a second. I think I've ranted on.

Firstly, no, that was really, really fantastic. And I think helped elucidate, you know, one of the major issues I do, I am concerned now that like I can feel job listings going up as we speak for AI kings now. And that makes me slightly, slightly uncomfortable. I also, I would have loved, I mean, you and I talk about evals and data a lot, and I know how you feel about them. Everyone here now knows as well. But I would have loved to be a fly on the wall when you first saw this, this figure and, and, and seen what, what happened.

I also, I do, I'm interested in all of your thoughts. It looks like there are just so many false dichotomies in this. I mean, it's, it's useful in some ways. But you know, if we're talking about product, we're clearly talking about evals as well. In some sense, or hopeful, like some way of measuring the impact or effectiveness, or however you're measuring a product, right? So I do feel like there are some false dichotomies there.

I, I am also interested. Actually, so Eugene you got to ask your question to Shreya. Shreya, you've prepared a question for Eugene as well, which I think will help us step back and consider the report as a whole.

Yeah. Okay. Eugene, my question was, as, as you kind of primarily led this effort, and it exploded into, I don't even know how many lessons, if you had to pick, if this report could only be about three lessons, which three would they be?

All right. So I think the first one I would think of, so I'm going to try to pick three lessons to what I think has brought the most value to people every time I spoke about them. I think the first one is going to be evals. I mean, I was just talking to a founder yesterday, not I think Tuesday, and he was telling me about here. Here's how my, here's how my process looks. Here's, here's how my team's process looks. And I was like asking him, why do you only do evals at the end?

It's like, wait, that's not what we're supposed to do. Like we build a product and you're like, no, but why are you not evaluating throughout your development cycle? It's like, huh, what do you think about that? Because it's like almost like a training or machine learning model and machine learning model is the artifact is the product you do the eval at the end, I guess. But now you're building a product, you do the eval throughout your iteration cycle, as you update your reg, as you update your fine tuning, as you update your product, you do the eval.

I think the second thing is lexical search. So I'm on this soapbox. I think Joe is also on this soapbox. Not everyone agrees, but I really think that if you, everyone should have BM25 as a baseline. So now that may not work, but most of the time it does. I think here's a story whereby there was a team that was like asking me, hey, Eugene, how can we improve our retrieval? And I asked them, what are you using? I said, obviously using embeddings like some embeddings on the hugging phase. I said, why don't you try to consider BM25?

So I was pretty insistent about it, like, okay, try it and then let me know how it goes. So the next time they got back to me, I think like one or two weeks later, they said, hey, Eugene, did you know that BM25 accounts for 80% of our retrieved documents? Relevant documents? Flip it the other way. If they were not using BM25, they left 80% of the juice on the table. It's like, holy crap, that's a lot. BM25 is such an easy and mindless baseline, very easy to tune. I mean, you don't even need to tune it, honestly, just use it.

I think the last one is, I think really much salient because of what happened today. Today, about 3.5 solid dropped. Okay, we're going to update the model, just change the model ID. I think the point here I'm trying to make is that the models will keep coming and go, when Lama 4 drops, Hamo is going to start his fine-tuning pipeline, BAM is going to be done, or like GPT 3.7, Hamo is going to kick off his fine-tuning pipeline. The models will come and go, but what's constant? Your evals, your guardrails, your fine-tuning pipeline, your retrieval system, these are your mode, the durable parts of your system. The model is not.

So a lot of times, so the thing is, some teams are like, okay, this model is not good enough, let's start to fine-tune our model and they place all the bets on the model. It's all about the model, but no, I think it's really to think about your pipeline that generates the model, which is the artifact. Your eval, that evaluates the model, your retrieval system that augments the model with context. I think that makes a more durable system in the long run. It's just lower effort in the long run. So that's my three things. Are you satisfied, Shreya?

Yeah. Well, the evals thing is very unsatisfying to me, not for anything Eugene says, but just the fact that we all talk so much about it and still it's such a problem, it makes me wonder, what are we doing? It's sometimes like, for example, for me, I am crippled if I don't have evals when I start a new use case. I mean, how would I try to retrieve? So sometimes I'm advising someone, I'm asking them, how do you know if you're getting better?

Sometimes they don't, they just look at us like, oh my God, dude, that's so tiring. You look at it over time, you just get numb. You need a way, like an assertion-based way, a programmatic way to evaluate it. I mean, I'm just lazy. But for the audience, I mean, do try it. Having the evals up front, as your insurance harness, your test harness just simplifies your production, simplifies your development cycle.

Yeah, absolutely. I would say about evals is like, okay, again, I predict that roughly a third of people when we have this podcast be published, be like, okay, evals, they're gonna look up evals and be like, okay, what are the, like, let me get the tools, like, what are the generic evals? Oh yeah, there's this like conciseness metric in this toxicity metric. And they're gonna like pull all the generic evals off the shelf and be like, yeah, I got evals. That is actually worse, probably, than doing evals.

So it's like, again, it's like domain specific evals for your problem. And also looking at data. So what I tell people all the time is like, don't be lazy. You have to look at your data. People this dichotomy is like, okay, there's AI like automates everything in life. But it doesn't automate looking, you have to look at your data. Like, otherwise, you don't know if something is going wrong, or you have to look at it for debugging. And that that's the part that I think, yeah, that's like a very interesting gap that people succumb to. They just want a tool that just does it, like, let me just do it with some pip install something.

And I checked that list that Hamel said, like, okay, I'm doing it. No. To some extent, I understand this mentality, though, because it feels like AI should be able to help you look at your data. I think it's very funny that the AI engineering job description or whatever that the diagram is does not have data literacy on it. As you said, Hamel, like data literacy means you can look at your outputs and your inputs, and make conclusions about them that quantify your performance that can help you drive up the performance stuff like that.

It feels like AI should be able to help you do this. But I don't, I don't think people should rely on, like, chativity or AI to look at your data. It's very interesting you said that. Like, I was talking with Brian Bischoff, who's going to be on this panel after us. So Brian Bischoff actually posted a job titled AI engineer very early on in this cycle. And he was like, hey man, like, you hate this job title so much, like, but I, you know, we kind of went back and forth. And I drilled into like, okay, how in the hell is it working for you? Because usually when people post the job title AI engineer is basically saying you want a unicorn and it doesn't really work out.

But for him, it worked out because Brian is a machine learning engineer and his process like, okay, concretely, one of his tests are about cleaning data, like take home exam is cleaning data. So already if you're giving someone, so Brian is probably like, very rare in terms of a hiring manager that's giving someone a take home doing cleaning data. Like, that takes a lot, that's like very thoughtful. That like, you know, he's correcting for I think a lot of things. And it's actually that's why it like works really well. He's like has a superb process.

And it also suggests as Brian's definition of data AI engineer includes data literacy, which is different from the graphic that Hammock showed, right? So I think there's different definitions of AI engineer. Brian happened to cover, Brian thoughtfully covered data literacy, which I completely agree is absolutely essential. And I found it not so easy to treat. I also, I just love that we can say Brian says anything right now, I've got so many things I want to say Brian's Brian's into, but to put more words in Brian's mouth as well, we can when he arrives, we can explore this further.

But I feel like something Brian would say is look at your data in notebooks as well, right? Like data literacy for him and for him, notebooks are one of the best, well, no, the best eval tool. But you know, when you're generating data or you've got data you're playing with, get it in a notebook, explore it, experiment with it, and then start to automate things and validate things more programmatically. For example, I mean, I think he might even say that notebooks are magic.

Okay, bad joke. I don't know if anyone got the pun, but yeah, I mean, he has this thing, he's building a tool called magic. Great, great joke, Eugene. And I will cast the hex on all of you with my notebooks. I also put two links in the show notes. And sorry, in the YouTube chat. One is Hamels post your AI product needs evals. Seeing this is a panel about evals now. But no, more seriously, this provides a very nice way of thinking through how to how to softly and slowly build up evals into your system.

And it's actually fun. We, Hamel and I talked about all of this on a podcast last year. And kind of came up with the story just beforehand, then had Emil from read chat join as well. And I remember Shreya was in, in the chat and really, like forcing Hamel to, to break down his ideas more, which led to this, this blog post. I also shared a link to Eugene's prompting fundamentals and how to apply them effectively. Also, like read these blogs all the time. I think these guys have newsletters as well. Follow them on Twitter. I mean, I can't, can't get enough, but I do, I do want to step back a bit because there are several other moving parts of the report that I really like.

And I'd like your thoughts on stepping back from the more technical side of things. You all discuss the importance of building trust with stakeholders and users when deploying AI powered software or LM, LM powered applications. What strategies or best practices have you found effective for establishing and maintaining trust?

Yeah, get people in the room. I think that's one, like one point that I liked was like, yeah, get designers and UX people in the room from the beginning. I think we, a lot of the implicit position of the report is for applications where the developers are sufficient domain experts to confidently grade LM outputs. But for, you know, medicine or law or other like very specialized that might not be the case. And that so like getting those people in allows you to find the like shibbolets or the like very easy low hanging fruit that like, you know, if you violate that, you will lose their trust.

And like, yeah, to sort of co design with them. I think, yeah, there's some good stuff from Kerry Kai, who does a lot of great like human computer interaction work at like Google and with folks at Stanford, that sort of talks about a lot of techniques for sort of like bringing these people in involving them in application development.

Yeah, and I guess maybe rolling stuff out slowly so that you can kind of like, I think frequently, like issues or problems are discovered sort of after several iterations of interaction. And so if you like roll something out to a small group, somebody in that small group will interact at least 10 times with the system and then discover this bad pattern. So there's like more value to that like repeated measures interaction than to going to 10 times as many users at the beginning. And so that allows you like that gives you like a benefit of operating at that smaller scale at first.

And to like correct issues before like you tell people to eat pizza with glue on it. Like you only tell like one person who's your friend to eat pizza with glue on it and then they like help you fix it instead of dunking on you on social media. Absolutely. Brian, is there anything you'd like to add to that?

I think the antidote for demoitis is user feedback. Like last summer, I went to as many of the like little AI meetups as I possibly could go to and my motivation was not like to eat like really crappy finger food. It was actually to like just like quickly put like, turn my laptop around and like do one thing with magic and see how people reacted.

And like, this was like while we had an active beta going on, but just like seeing people's reactions to different things, super, super interesting. I had people who like immediately were like, I don't know what's happening. And I was like, okay, great, that's lovely to hear. And then I had people that were very like, you know, immediately like, can I do this? Can I do this? And this was while we were sort of like building a new product in secret. And so I couldn't show the new product, but I was just like gaining feedback with the thing that we already had a beta and seeing how people were like thinking about what it was doing.

I learn an absolute ridiculous amount from every bit of feedback that I get. And so I don't know, I'm terrified by people that are spending two years in stealth before launching anything. And I think like, as much as we're all tired of the like AI hype demo, what I am very excited for is the AI hype demo as a beta like sign up list that they start rolling it out to users. That's a whole different game.

Yeah, absolutely. And something we've been talking around also is building systems, focusing on systems and not models as well. And so Brian, I know you have a lot of experience building end to end systems with LLM.

So I'm wondering if you could share an example or ideas of examples where a systems level view was particularly important for achieving the goals of the project?

Yeah, I mean, you know, I started at HEX the last day of February 2023. And at the time, there was one engineer on my team. And he flew to California like, I think it was two weeks later. And we went to the light board and drew out our like prompt templating architecture, our evaluation architecture, and our like context construction and RAG architecture. That was like what we did with that week. And the RAG architecture is still in prod with a lot of changes to like, certain aspects of it, but like the fundamental architecture, the prompt architecture has changed almost all, including the like appendix thing that we have, which is like, we inserted this thing into our system called a conformer layer.

And we were like, this is going to be really important. And like, it's very much an appendix in the sense of like, it has, it has a purpose. But like, it sure is easy to misunderstand why. And then like, our eval architecture, like that lasted us nine months. And then we ultimately did have to rewrite that. But like, seeing ML systems meant that like two weeks into this job, I was like, evals are important. Like, like, I know that evals are important. Building something that's like opposability first for our like, context construction is important. And then thinking about like, our prompt construction, like flow, as like, essentially like metaprogramming, like, that was, those were the three things that I was just like, cool, stealing this from my previous experience.

And then, of course, the rag is Rex's thing. Like, yeah, that's it. And those were all things that I just pulled from like textbook ML, if you go and you pull down the, the, the book, machine learning design patterns, like everything that I said in my first like months at hex was like, could have pulled it straight from that book. Shout out to the authors of that wonderful book, it's still my all time favorite O'Reilly book.

Yeah, hopefully not your all time favorite O'Reilly document, though. So I would say about evals is like, okay, again, I predict that roughly a third of people when we have this podcast be published, be like, okay, evals, they're gonna look up evals and be like, okay, what are the, like, let me get the tools, like, what are the generic evals? Oh yeah, there are this like conciseness metric in this toxicity metric. And they're gonna like pull all the generic evals off the shelf and be like, yeah, I got evals. That is actually worse, probably, than doing evals.

So it's like, again, it's like domain specific evals for your problem. And also looking at data. So what I tell people all the time is like, don't be lazy. You have to look at your data. People this dichotomy is like, okay, there's AI like automates everything in life. But it doesn't automate looking, you have to look at your data. Like, otherwise, you don't know if something is going wrong, or you have to look at it for debugging. And that that's the part that I think, yeah, that's like a very interesting gap that people succumb to.

They just want a tool that just does it, like, let me just do it with some pip install something. And I checked that list that Hamel said, like, okay, I'm doing it. No, to some extent, I understand this mentality, though, because it feels like AI should be able to help you look at your data. I think it's very funny that the AI engineering job description or whatever that the diagram is does not have data literacy on it. As you said, Hamel, like data literacy means you can look at your outputs and your inputs and make conclusions about them that quantify your performance that can help you drive up the performance stuff like that.

It feels like AI should be able to help you do this. But I don't, I don't think people should rely on, like, chativity or AI to look at your data. It's very interesting you said that.

Like, I was talking with Brian Bischoff, who's going to be on this panel after us. So Brian Bischoff actually posted a job titled AI engineer very early on in this cycle. And he was like, hey man, like, you hate this job title so much, like, but I, you know, we kind of went back and forth. And I drilled into like, okay, how in the hell is it working for you? Because usually when people post the job title AI engineer is basically saying you want a unicorn and it doesn't really work out.

But for him, it worked out because Brian is a machine learning engineer and his process like, okay, concretely, one of his tests are about cleaning data, like take home exam is cleaning data. So already if you're giving someone, so Brian is probably like, very rare in terms of a hiring manager that's giving someone a take home doing cleaning data.

Like, that takes a lot, that's like very thoughtful. That like, you know, he's correcting for I think a lot of things. And it's actually that's why it like works really well. He's like has a superb process.

And it also suggests as Brian's definition of data AI engineer includes data literacy, which is different from the graphic that Hammock showed, right? So I think there's different definitions of AI engineer. Brian happened to cover, Brian thoughtfully covered data literacy, which I completely agree is absolutely essential. And I found it not so easy to treat. I also, I just love that we can say Brian says anything right now, I've got so many things I want to say Brian's Brian's into, but to put more words in Brian's mouth as well, we can when he arrives, we can explore this further.

But I feel like something Brian would say is look at your data in notebooks as well, right? Like data literacy for him and for him, notebooks are one of the best, well, no, the best eval tool. But you know, when you're generating data or you've got data you're playing with, get it in a notebook, explore it, experiment with it, and then start to automate things and validate things more programmatically.

For example, I mean, I think he might even say that notebooks are magic.

Okay, bad joke. I don't know if anyone got the pun, but yeah, I mean, he has this thing, he's building a tool called magic. Great, great joke, Eugene. And I will cast the hex on all of you with my notebooks. I also put two links in the show notes. And sorry, in the YouTube chat.

One is Hamels post your AI product needs evals. Seeing this is a panel about evals now. But no, more seriously, this provides a very nice way of thinking through how to how to softly and slowly build up evals into your system. And it's actually fun. We, Hamel and I talked about all of this on a podcast last year and kind of came up with the story just beforehand, then had Emil from read chat join as well.

And I remember Shreya was in, in the chat and really, like forcing Hamel to, to break down his ideas more, which led to this, this blog post. I also shared a link to Eugene's prompting fundamentals and how to apply them effectively. Also, like read these blogs all the time. I think these guys have newsletters as well. Follow them on Twitter. I mean, I can't, can't get enough, but I do I do want to step back a bit because there are several other moving parts of the report that I really like. And I'd like your thoughts on stepping back from the more technical side of things.

You all discuss the importance of building trust with stakeholders and users when deploying AI powered software or LM, LM powered applications. What strategies or best practices have you found effective for establishing and maintaining trust?
Yeah, get people in the room. I think that's one, like one point that I liked was like, yeah, get designers and UX people in the room from the beginning. I think we, a lot of the implicit position of the report is for applications where the developers are sufficient domain experts to confidently grade LM outputs. But for, you know, medicine or law or other like very specialized that might not be the case. And that so like getting those people in allows you to find the like shibbolets or the like very easy low hanging fruit that like, you know, if you violate that, you will lose their trust.

And like, yeah, to sort of co design with them. I think, yeah, there's some good stuff from Kerry Kai, who does a lot of great like human computer interaction work at like Google and with folks at Stanford, that sort of talks about a lot of techniques for sort of like bringing these people in involving them in application development.

Yeah, and I guess maybe rolling stuff out slowly so that you can kind of like, I think frequently, like issues or problems are discovered sort of after several iterations of interaction.

And so if you like roll something out to a small group, somebody in that small group will interact at least 10 times with the system and then discover this bad pattern. So there's like more value to that like repeated measures interaction than to going to 10 times as many users at the beginning. And so that allows you like that gives you like a benefit of operating at that smaller scale at first.

And to like correct issues before like you tell people to eat pizza with glue on it. Like you only tell like one person who's your friend to eat pizza with glue on it and then they like help you fix it instead of dunking on you on social media. Absolutely. Brian, is there anything you'd like to add to that?

I think the antidote for demoitis is user feedback. Like last summer, I went to as many of the like little AI meetups as I possibly could go to and my motivation was not like to eat like really crappy finger food. It was actually to like just like quickly put like, turn my laptop around and like do one thing with magic and see how people reacted.

And like, this was like while we had an active beta going on, but just like seeing people's reactions to different things, super, super interesting. I had people who like immediately were like, I don't know what's happening. And I was like, okay, great, that's lovely to hear. And then I had people that were very like, you know, immediately like, can I do this? Can I do this? And this was while we were sort of like building a new product in secret. And so I couldn't show the new product, but I was just like gaining feedback with the thing that we already had a beta and seeing how people were like thinking about what it was doing.

I learn an absolute ridiculous amount from every bit of feedback that I get. And so I don't know, I'm terrified by people that are spending two years in stealth before launching anything. And I think like, as much as we're all tired of the like AI hype demo, what I am very excited for is the AI hype demo as a beta like sign up list that they start rolling it out to users. That's a whole different game.

Yeah, absolutely. And something we've been talking around also is building systems, focusing on systems and not models as well. And so Brian, I know you have a lot of experience building end to end systems with LLM.
So I'm wondering if you could share an example or ideas of examples where a systems level view was particularly important for achieving the goals of the project?

Yeah, I mean, you know, I started at HEX the last day of February 2023. And at the time, there was one engineer on my team. And he flew to California like, I think it was two weeks later. And we went to the light board and drew out our like prompt templating architecture, our evaluation architecture, and our like context construction and RAG architecture. That was like what we did with that week. And the RAG architecture is still in prod with a lot of changes to like, certain aspects of it, but like the fundamental architecture, the prompt architecture has changed almost all, including the like appendix thing that we have, which is like, we inserted this thing into our system called a conformer layer.
And we were like, this is going to be really important. And like, it's very much an appendix in the sense of like, it has, it has a purpose. But like, it sure is easy to misunderstand why.

And then like, our eval architecture, like that lasted us nine months. And then we ultimately did have to rewrite that. But like, seeing ML systems meant that like two weeks into this job, I was like, evals are important.

Like, like, I know that evals are important. Building something that's like opposability first for our like, context construction is important. And then thinking about like, our prompt construction, like flow, as like, essentially like metaprogramming, like, that was, those were the three things that I was just like, cool, stealing this from my previous experience. And then, of course, the rag is Rex's thing.

Like, yeah, that's it. And those were all things that I just pulled from like textbook ML, if you go and you pull down the, the, the book, machine learning design patterns, like everything that I said in my first like months at hex was like, could have pulled it straight from that book. Shout out to the authors of that wonderful book, it's still my all time favorite O'Reilly book.

Yeah, hopefully not your all time favorite O'Reilly document, though. So I would say about evals is like, okay, again, I predict that roughly a third of people when we have this podcast be published, be like, okay, evals, they're gonna look up evals and be like, okay, what are the, like, let me get the tools, like, what are the generic evals?

Oh yeah, there are this like conciseness metric in this toxicity metric. And they're gonna like pull all the generic evals off the shelf and be like, yeah, I got evals. That is actually worse, probably, than doing evals.

So it's like, again, it's like domain specific evals for your problem. And also looking at data. So what I tell people all the time is like, don't be lazy. You have to look at your data. People this dichotomy is like, okay, there's AI like automates everything in life.

But it doesn't automate looking, you have to look at your data. Like, otherwise, you don't know if something is going wrong, or you have to look at it for debugging. And that that's the part that I think, yeah, that's like a very interesting gap that people succumb to.

They just want a tool that just does it, like, let me just do it with some pip install something. And I checked that list that Hamel said, like, okay, I'm doing it. No, to some extent, I understand this mentality, though, because it feels like AI should be able to help you look at your data.

I think it's very funny that the AI engineering job description or whatever that the diagram is does not have data literacy on it. As you said, Hamel, like data literacy means you can look at your outputs and your inputs and make conclusions about them that quantify your performance that can help you drive up the performance stuff like that.

It feels like AI should be able to help you do this. But I don't, I don't think people should rely on, like, chativity or AI to look at your data. It's very interesting you said that.

Like, I was talking with Brian Bischoff, who's going to be on this panel after us. So Brian Bischoff actually posted a job titled AI engineer very early on in this cycle. And he was like, hey man, like, you hate this job title so much, like, but I, you know, we kind of went back and forth. And I drilled into like, okay, how in the hell is it working for you? Because usually when people post the job title AI engineer is basically saying you want a unicorn and it doesn't really work out.

But for him, it worked out because Brian is a machine learning engineer and his process like, okay, concretely, one of his tests are about cleaning data, like take home exam is cleaning data.

So already if you're giving someone, so Brian is probably like, very rare in terms of a hiring manager that's giving someone a take home doing cleaning data. So already it's like, okay, yeah.

Well, I actually find that super interesting. And I want to thank everyone who came on the panel today. Thank you guys for your time. Amazingly, I do want to say the first question felt like the, like introducing the project or the paper, but the second half felt like a very productive workshop. So I hope to steal a page from your book in the future. I'm going to finally wrap it up.

I want to thank everyone for tuning in and engaging with us. It's been a wonderful time. Thank you all.

<!-- Keywords -->
#collaboration
<!-- /Keywords -->
