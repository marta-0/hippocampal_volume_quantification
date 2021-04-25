## Project Instructions

### Section 3: Integrating into a clinical network

<img src="ohif.png" width=400em>

In this final section you will use some of the work you did for Section 2 to create an AI product that can be integrated into a clinical network and provide the auto-computed information on the hippocampal volume to the clinicians. While hospital integrations are typically handled by hospital IT staff, it will help tremendously if you can talk the same language with the people who will operate your model, and will have a feel for how clinical radiological software works. These skills will also help you debug your model in the field.

You will perform this section in a different workspace than the previous two sections: **Workspace 2**. This workspace is a simpler hardware, with no GPU, which is more representative of a clinical environment. This workspace also has a few tools installed in it, which is replicates the following clinical network setup:

<img src="network_setup.png" width=400em>

Specifically, we have the following software in this setup:

* MRI scanner is represented by a script `section3/src/deploy_scripts/send_volume.sh`. When you run this script it will simulate what happens after a radiological exam is complete, and send a volume to the clinical PACS. Note that scanners typically send entire studies to archives.
* PACS server is represented by [Orthanc](http://orthanc-server.com/) deployment that is listening to DICOM DIMSE requests on port 4242. Orthanc also has a DicomWeb interface that is exposed at port 8042, prefix /dicom-web. There is no authentication and you are welcome to explore either one of the mechanisms of access using a tool like curl or Postman. Our PACS server is also running an auto-routing module that sends a copy of everything it receives to an AI server. See instructions ad the end of this page on how to launch if you are using the Udacity Workspace.  
* Viewer system is represented by [OHIF](http://ohif.org/). It is connecting to the Orthanc server using DicomWeb and is serving a web application on port 3000. Again, see instructions at the end of this page if you are using the Udacity Workspace.
* AI server is represented by a couple of scripts. `section3/src/deploy_scripts/start_listener.sh` brings up a DCMTK's `storescp` and configures it to just copy everything it receives into a directory that you will need to specify by editing this script, organizing studies as one folder per study. HippoVolume.AI is the AI module that you will create in this section.

If you want to replicate this environment on your local machine, you will find instructions in the Project Overview concept.

As with Section 2, in the directory called `section3/src` you will find the source code that forms the skeleton of the HippoVolume.AI module.

`inference_dcm.py` is the file that you will be working on. It contains code that will analyze the directory of the AI server that contains the routed studies, find the right series to run your algorithm on, will generate report, and push it back to our PACS.

Note that in real system you would architect things a bit differently. Probably, AI server would be a separate piece of software that would monitor the output of the listener, and would manage multiple AI modules, deciding which one to run, automatically. In our case, for the sake of simplicity, all code sits in one Python script that you would have to run manually after you simulate an exam via the `send_volume.sh` script - `inference_dcm.py`. It combines the functions of processing of the listener output and executing the model, and it does not do any proper error handling :)

As before, you will need to follow the instructions inside the code files to complete the section and create your AI module. Same convention is used as in Sections 1 and 2: comments that start with `# TASK` instruct you to create certain code snippets, and all other types of comments provide background or stand-out suggestions.

You will need to complete all the instructional comments in the code in order to complete this section. You can do this in any order, but it makes most sense to start with the code in `inference_dcm.py`.

Once you complete the code, you can test it by running
> `deploy_scripts/send_volume.sh`

which will simulate a completion of MRI study and sending of patient data to our PACS, and then following that by running `inference_dcm.py`

The `send_volume.sh` script needs to be run from directory `section3/src` (because it relies on relative paths). If you did everything correctly, an MRI scan will be sent to the PACS and to your module which will compute the volume, prepare the report and push it back to the PACS so that it could be inspected in our clinical viewer.

At this point, go to *[YOUR IP ADDRESS]*:3000 (can be another port if you are using Udacity Workspace) which brings up our OHIF viewer. You should be able to inspect your report in all its glory, in the context of a radiological study presented to a radiologist in a clinical viewer!

The study that `send_result.sh` sends, and a few other sample studies are located in `/data/TestVolumes`. Feel free to modify the script to try out your algorithm with other volumes.

> Note, that the DICOM studies used for inferencing this section have been created artificially, and while full-brain series belong to the same original study, this is not the study from which the hippocampus crop is taken.

Now that you have built a radiological AI system and given it to clinicians, you can start collecting data on how your model performs in the real world. If you (or the company you work for) intends to commercialize your technology, you will have to clear the regulatory bar. As we have discussed in our final lesson, an important contribution of an AI engineer to this endeavor is helping execute the clinical validation by contributing to a validation plan. Your final task in this course is to write a draft of such plan (shoot for 1-2 pages for this exercise). Remember - clinical validation is all about proving that your technology performs the way you claim it does. If you are saying that it can measure hippocampal volume, your validation needs prove that it actually does, and establish the extents to which your claim is true. Your validation plan needs to define how you would prove this, and establish these extents.

For the purpose of this exercise, assume that you have access to any clinical facility and patient cohorts you need, and that you have all the budget in the world. Assume that you know where your data came from and that you know how to label it (just come up with a good story). In your plan, touch on at least the following:

* Your algorithm relies upon certain "ground truth" - how did you define your ground truth? How will you prove that your method of collecting the ground truth is robust and represents the population that you claim this algorithm is good for?
* How do you define accuracy of your algorithm and how do you measure it with respect to real world population? Check out the [calculator and report from HippoFit](http://www.smanohar.com/biobank/calculator.html) for some inspiration.
* How do you define what data your algorithm can operate on?

There is no right answer here - think of these and other questions that would come up during validation of such algorithm. Thinking of such things early on will help you build better algorithms in the first place.

#### Expected Outcome

Navigate to the directory `section3/out` to find the [README.md](section3/out/README.md) with instructions on what is expected as the outcome.
