from flask import Blueprint, render_template_string, request, redirect, flash, render_template
import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt
from sko.ACA import ACA_TSP
import mpld3
import os
from website import views
import random
from google.cloud import storage
import io
from urllib.error import HTTPError


auth = Blueprint('auth', __name__)

@auth.route('/Holders')
def articles():
    return render_template('experiences.html')






