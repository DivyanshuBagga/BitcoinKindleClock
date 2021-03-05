This project is derived from [kindle-display](https://github.com/dennisreimann/kindle-display). If you have a spare old kindle, and this seemed like a good way to put it use. The idea is to hack your kindle to fetch and display a greyscale image from server. In turn, the server fetches the bitcoin price and blockchain height from various sources to create the desired image. You can include any piece of interesting information on the image, for example a random [bitcoin quote](https://www.bitcoin-quotes.com).

We will Configure kindle exactly as described in [kindle-display](https://github.com/dennisreimann/kindle-display), but instead of setting a local server, we will set it on Amazon EC2 machine. The EC2 machine will generate and place the image on Amazon S3 bucket with public access. You may skip the server setup entirely, point your kindle to fetch the [display.png](http://divyanshubagga.s3-website.us-east-2.amazonaws.com/display.png) that has been set to refresh every 10 minutes.

# Configure Kindle

1. Jailbreaak your kindle using package and instruction from [mobileread forum](https://www.mobileread.com/forums/showthread.php?t=225030).
2. Install the following packages:

  - USBNetwork
  - MKK
  - KUAL

3. Activate USBNetwork. This requires putting kindle in debug mode and executing command ~usbNetwork. Turn off debug mode after enabling USBNetwork.
4. Connect your kindle through ssh, and run the commands in [paste-to-install.sh](https://github.com/dennisreimann/kindle-display/blob/master/kindle/paste-to-install.sh). Specify the server address, by setting SERVER, before pasting the commands.
\end{enumerate}

# Configure Server
The following steps assume you hace an Amazon Linux EC2 instance.

1. Copy server folder and cron.sh from the github repository to EC2 machine. Make sure cron.sh is in the parent folder of server folder.
2. Update path in cron.sh. 
3. Create an S3 bucket, with policy which enables public access.
4. Create a IAM EC2 role which has full access to S3. Assign the role to your EC2 instance containing update.py.
5. Run sudo crontab -e on EC2. Enter the insert mode by pressing 'i', and paste the following:
```shell
SHELL=/bin/bash
PATH=/bin:/usr/bin:/usr/local/bin
*/10 * * * * /home/ec2-user/Bitcoin/cron.sh >> /home/ec2-user/Bitcoin/cron.log 2>&1
```
Quit by pressing 'Esc', followed by 'wq'. Now your cron job is set to generate display.png, in the S3 bucket, every 10 minutes.

