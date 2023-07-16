# Choose a cloud provider for deployment ☁️

Now, we need a place to host our container.
However, we don't want to manage our own servers (I only brought my laptop 🤷). We will therefore have to use a cloud provider to host our container.

There are many providers to choose from. Just to name a few:
- [Azure](https://azure.microsoft.com/en-us/)
- [Google Cloud](https://cloud.google.com/)
- [AWS](https://aws.amazon.com/)
- [Digital Ocean](https://www.digitalocean.com/)
- [IBM Cloud](https://www.ibm.com/cloud/)
- [Oracle Cloud](https://www.oracle.com/cloud/)
- [Alibaba Cloud](https://www.alibabacloud.com/)
- [Linode](https://www.linode.com/)
- [Vultr](https://www.vultr.com/)
- [Heroku](https://www.heroku.com/)

For this tutorial, we have extensively worked out the steps for **Azure** and **Google Cloud (GCP)**, but similar steps should be possible for other cloud providers as well. You are free to to choose the direction you take from here.

However, the challenge for today is that most providers, if not all, require you to enter your credit card details to get started.

Some of them offer a free trial or ~$200 free credit, but you still have to enter your credit card details to get started...

That's why for this workshop, you can **choose one of these options**:
1. Use your company's cloud provider account, if you have the necessary permissions to spin up resources.
2. (*recommended*) Create a new account on a cloud provider of your choice, and enter your credit card details. You can always delete your account afterwards. You get free money, you can set budget alerts, and for example Azure and Google will not even charge you unless you explicitly upgrade your account.
3. Collaborate with someone next to you who went for option 1 or 2 above.
4. Listen in and follow along as we deploy your container to the cloud on the big screen!

In the following, we describe the steps for deployment on Azure and GCP, assuming we start with a fresh account. We will deploy our app first through the cloud provider's user interface (UI), and then through the command line interface (CLI) from our local machine.

See exercises `08a`, `08b`, and `08c`, and pick the one that's applicable to you!
