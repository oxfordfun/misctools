cp nodes nodes.txt
python3 dumpnodes.py > nodes
systemctl --user restart catgrid
sleep 5
cat nodes | python3 loadnodes.py
