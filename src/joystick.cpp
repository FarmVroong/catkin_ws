#include<ros/ros.h>
#include<geometry_msgs/Twist.h>
#include<sensor_msgs/Joy.h>
#include<iostream>

using namespace std ;

class TeleopJoy{
	public:
		TeleopJoy();
	private: 
		void callBack( const sensor_msgs ::Joy::ConstPtr& Joy ); 
		ros::NodeHandle n; 
		ros::Publisher Pub; 
		ros::Subscriber Sub; 
		int i_velLinear , i_velAngular ;
};

TeleopJoy::TeleopJoy()
{ 	
	n.param("axis_linear", i_velLinear , i_velLinear ); 
	n.param("axis_angular", i_velAngular , i_velAngular );
	
	// Pub = n- . Advertise < turtlesim ::Velocity>("turtle1/command_velocity",1);
	// Sub = n- . Subscribe < sensor_msgs ::Joy>("joy", 10, &TeleopJoy:: callBack , the this ); 
    Pub = n.advertise <geometry_msgs::Twist>("/cmd_vel",1); 
	Sub = n.subscribe <sensor_msgs::Joy>("joy", 10, &TeleopJoy:: callBack , this );
}

void TeleopJoy::callBack( const sensor_msgs ::Joy::ConstPtr& Joy )
{
	// turtlesim ::Velocity Vel ; 
    geometry_msgs::Twist Vel ; 
	Vel.angular.z = Joy -> axes [ i_velAngular ]; 
	Vel.linear.x =Joy -> axes [ i_velLinear ]; 
	Pub.publish( Vel );
	// Vel . Angular = Joy -> axes [ i_velAngular ];
	// Vel . Linear = Joy -> axes [ i_velLinear ];
	// Pub .publish( Vel );
}

int main( int argc , char **argv )
{ 
	ros::init( argc , argv , "TeleopJoy");
	TeleopJoy teleop_turtle ;

	ros::spin();
}
