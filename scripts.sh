ludwig train --dataset training_data.csv --config "{input_features: [{name: video_title, type: text}], output_features: [{name: class, type: category}]}"

ludwig visualize --visualization learning_curves --training_statistics results/experiment_run/training_statistics.json


ludwig predict --dataset kaggle_data/Youtube_Videos_USA.csv --model_path results/experiment_run/model


ludwig evaluate --dataset testing_data.csv --model_path results/experiment_run/model

ludwig visualize --visualization compare_performance --test_statistics results/test_statistics.json 
