**Hello**🖐 **Automated Testing for Curahealthcare Demo Website with Selenium (Pytest, POM, HTML Reports, Jenkins Pipeline)**

This project tests the functionalities of CuraHealthcare, including valid and invalid login attempts, viewing history, and managing appointments.
___________________________________________

🎯 **Pre-requisites:**
- Python 3
- Any browsers(Chrome, Firefox, Edge)
___________________________________________

▶ **Test Execution**

Run commands: 
1. Install Dependecies:

       pip install -r requirements.txt
2. Run the test with html report:

       pytest -v --html=report.html 
   or specifying browser

       pytest -v --browser=edge --html=report.html
    

**To run this on jenkins**
1. Add item name, click Pipeline and click OK
   ![img_1.png](img_1.png)
2. Scroll down and navigate to Pipeline then select "pipeline script from SCM"
   ![img_2.png](img_2.png)
3. Select Git
   ![img_3.png](img_3.png)
4. Paste the URL and click Apply and Save
   ![img_4.png](img_4.png)
5. Click build now
   ![img_5.png](img_5.png)



    
   
   
    
