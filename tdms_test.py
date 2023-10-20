import nptdms

tdms_file_path = './sample.tdms'

with nptdms.TdmsFile.read(tdms_file_path) as tdms_file:
    print("-"*100)
    groups = tdms_file.groups()
    # Print group names
    for group in groups:
        print(f"Group Name: {group.name}")
        print("-"*100)
        # List all channels in the group
        channels = group.channels()
        
        # Print channel names
        for channel in channels:
            print("-"*100)
            print(f"Channel Name: {channel.name}")
            
            # Access and print data from the channel
            data = channel[:]
            print(f"Data: {type(data)}")
            print(data)
