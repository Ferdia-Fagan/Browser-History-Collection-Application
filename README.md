<h1>Browser-History-Collection-Application</h1>

<h2>Introduction</h2>

<p>Hi, I am a final year CS undergraduate. I am working on my fianl year project this year.
For my final year project, I am building a tool to aid PC users to use their OWN browser history 
to aid them in looking back through their history for things they have seen, etc. 
This will be a tool to help people research and learn things online.</p>

<p> I like to think of it as a way to ease the pressure and mistakes of a users biological RAM,
  when researching things online. It sucks forgetting where you saw something. 
  Hopefully this tool will help with that </p>
  
  <p>I am aiming the collection group to be computer scientists, mainly because they will be able
  to read the code and see I am not doing anything dodgy. But, this is not closed off to anyone.</p>
  
 <h2>What do I need from you?</h2>
 
 <p>I want autonomous browser history <b>from students, researchers, or anyone that uses the 
internet to learn.</b> I want browser history where you where actively researching something.</p>
  
  <p>I also need you to trust me, as I do know this does sound dodgy (but keep in mind, google and big tech
   are much more invasive and look at your data, and profit off it... 
    Firstly, there is very little information I can gather from looking 
  through firefox places.sqlite and chrome History (sqlite) that would be deemed as 
  "very personal data". I <b>wont</b> be taking login details, looking at cookies, etc. 
  I wont even be looking at the data very much. </p>
  <p><b>You are in control</b>, as you get to select a time frame of browser history 
  you want to cut out and give to me. </p>
  
  <p><b>I will not be collecting any statistics about you. All I want is to see
  is research paths in your browsing history</b></p>
  
  <h2>What do I not want from you?</h2>
  
  <p>I dont want browser history from when you where searching through youtube, or facebook, or ... anything weird...</p>
  <p>I dont want any personal data.</p> 
  <p>I dont want to use this data to do some kind of marketing or psychological analysis of you.</p>
  
  <p>I only collect what you can see in your browsing history (i.e. the search paths and link you use. And I only take a set of time you choose yourself.</p>
  
<h2>What is this project</h1>

<p>This python project is not my final year project. 
This is a tool to help me gather browser history data to complete and test my project.
As said above, I am making a tool to help PC users to have a better local browser/search history 
on there machine, so they can do queries and searches through information they have already seen/searched 
for.</p>

<h2>What will I use your data for?</h2>
<p>Your data will be Anonymous. So I wont know who you are when you send me the data.</p>

<p>This browser history data will then be fed into what is essentially a modified web crawler.
The browser history will be used to decide where the web crawler crawls to do its mining.</p>

<p>NOTE: Any browser history links that require a log in, and are not public, the web crawler will
not access. I couldn't access these links with the data I am gathering, even if I wanted to (and I dont).
Nor could I triangulate your location. </p>

 
<h2>How to use it</h2>

<p>Firstly, to run this program, your browser must be closed.</p>

<p>It is very simple. Download this project. Unzip. And run "UserClient.py" using command line.
Then, you will get instructions on how to proceed</p>

<p>NOTE:Do not ignore setting up providing paths to your browsers folders.</p>
<h5>link browsers</h5>
<p>To link with chrome: search "chrome://version/" , and copy the "Profile Path".</p>
<p>To link with firefox: 
    Click the menu button , click Help and select Troubleshooting Information. The Troubleshooting Information tab will open.
    Under the Application Basics section next to Profile Directory, click <b>Open Directory</b>. Your profile folder will open. </p>

<h5>Then you can run it<h5>

<p>Enter "load_my_data" command, and follow the prompts</p>

<p>Please enter the meta data about what it is you are researching. This will be helpful to me and 
will likely be the only part of your data I will look at..</p>

<p>You encrypted files will be in "user_folder" (sub folder of the applications folder).
Just send <b>user_folder</b> over to me after you zip it :)</p>

<p>You have the choice of emailing it to me (you will be prompted with my email) 
or sending it to a drop box link (private link). </p>

<h2>Thank you to everyone who submits data :)</h2>
<p>You have my word that I will not use your data in any way that makes
you feel I have lied to you, spied on you, or humiliate you. 
I will not snoop through anything.
I want to make a open source project, 
that I hope will expand beyond the final year project, to help make education
and learning cheaper, and more importantly more accessible to more people.</p>

<p>Thank you very much.</p>


