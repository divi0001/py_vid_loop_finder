import cv2
# import time
import json
def preprocess2(files,targets,i,j):
    
    orb = cv2.AKAZE_create()
    bf = cv2.BFMatcher()
    d = {}
    
    for k,fname in enumerate(files):
        if(k in range(0,i)) or (k in range (i+1,j)):
            continue
        vid = cv2.VideoCapture(fname)
        print(f"currently working on the video stored at {fname}")
        total = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"total frames: {total}")
        
        aka = []
        for g in range(total-1):
            aka.append([orb.detectAndCompute(cv2.cvtColor(vid.read()[1], cv2.COLOR_BGR2GRAY),None)[1],g])
        
        for i in range(0,total-1):
            # print(f"at {i}-th frame")
            # t1 = time.time()
            comp = list()
            desc1 = aka[i][0]
            for j in range(i+1,total-1):
                if(j>=total):
                    break
                desc2 = aka[j][0]
                # print(j)
                if desc1 is not None and desc2 is not None and len(desc2)>1 and len(desc1)>1:
                    matches = bf.knnMatch(desc1, desc2, k=2)
                    if len(matches)>1:
                        good_matches = [m for m, n in matches if m.distance < 0.75*n.distance]
                        if(len(good_matches)>0):
                            comp.append([sum(m.distance for m in good_matches)/len(good_matches),j])
                    else:
                        comp.append([matches,j])
            comp = sorted(comp, key = lambda x: x[0])[:10000]
            d[i] = comp
            # t2 = time.time()
            print(f"frame {i}")
            # print(f"needed {t2-t1} seconds or {(t2-t1)/60} minutes for the frame {i}")
        j = json.dumps(d)
        print("done, writing to file...")
        open(targets[k],'w').write(j)
        print("successfully written to file from targets(2)")
        
print("please input the file you want to process")
ii = int(input())
ii2 = int(input("The amount of files in the folder you want to process"))

targets = [f"just_for_fun/process_relax/processed/{i}.mp4" for i in range(7)]
targets2 = [f"just_for_fun/process_relax/processed/{i}.json" for i in range(7)] #just my folder structure, put your in and outputs in targets and targets2

preprocess2(targets, targets2,ii,ii2)

