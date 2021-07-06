/*
* Author: Jonathan Nushi
*/


#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "Point.h"

#define POINT_STRING_LENGTH (64)

typedef struct PointData {
    double x;
    double y;
    char to_string[POINT_STRING_LENGTH];
} PointData;

double Point_x(Point * this) {
    return this->data->x;
}

double Point_y(Point * this) {
    return this->data->y;
}

double Point_magnitude(Point * this) {
    return sqrt((Point_x(this), 2) + pow(Point_y(this), 2));
}

double Point_distance(Point * this, Point * that) {
    return sqrt(pow(Point_x(this) - Point_x(that), 2) + pow(Point_y(this) - Point_y(that), 2));
}

char * Point_to_string(Point * this) {
    return this->data->to_string;
}

void Point_delete(Point * this) {
    free(this->data);
    free(this);
}

void Point_init_data (Point * this, double x, double y) {
    this->data->x = x;
    this->data->y = y;
    sprintf(this->data->to_string, "(%f, %f)", x, y);
}

void Point_init_functions(Point * this) {
    this->x = &Point_x;
    this->y = &Point_y;
    this->to_string = Point_to_string;
    this->magnitude = &Point_magnitude;
    this->distance = &Point_distance;
    this->delete = &Point_delete;
}

Point * Point_new(double x, double y) {
    Point * point = (Point *)malloc(sizeof(Point));
    point->data = (PointData *)malloc(sizeof(PointData));
    Point_init_data(point, x, y);
    Point_init_functions(point);
    return point;
}